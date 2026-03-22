"""Módulo de búsqueda RAG para la Knowledge Base de Restaurantes."""

import os
import re
import uuid
from pathlib import Path
from typing import Optional

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm


class KnowledgeBase:
    def __init__(self, docs_dir: str):
        self.docs_dir = Path(docs_dir)
        self.chunks: list[dict] = []
        self.chunk_embeddings: Optional[np.ndarray] = None
        self.index: Optional[faiss.IndexFlatIP] = None
        self.model: Optional[SentenceTransformer] = None
        self.use_openai = bool(os.getenv("OPENAI_API_KEY"))

    async def initialize(self):
        self._load_documents()
        self._create_chunks()
        await self._build_index()

    def _load_documents(self):
        self.documents = {}
        for md_file in self.docs_dir.rglob("*.md"):
            try:
                relative_path = str(md_file.relative_to(self.docs_dir))
                content = md_file.read_text(encoding="utf-8")
                self.documents[relative_path] = content
            except Exception as e:
                print(f"Error leyendo {md_file}: {e}")

    def _create_chunks(self):
        chunk_size = 400
        chunk_overlap = 80

        for doc_path, content in self.documents.items():
            clean_content = self._clean_markdown(content)
            paragraphs = [p.strip() for p in clean_content.split("\n\n") if p.strip()]

            current_chunk = ""
            for para in paragraphs:
                if len(current_chunk) + len(para) < chunk_size:
                    current_chunk += "\n\n" + para
                else:
                    if current_chunk.strip():
                        self.chunks.append(
                            {
                                "id": str(uuid.uuid4()),
                                "content": current_chunk.strip(),
                                "source": doc_path,
                                "url": self._path_to_url(doc_path),
                            }
                        )
                    current_chunk = para

            if current_chunk.strip():
                self.chunks.append(
                    {
                        "id": str(uuid.uuid4()),
                        "content": current_chunk.strip(),
                        "source": doc_path,
                        "url": self._path_to_url(doc_path),
                    }
                )

    def _clean_markdown(self, text: str) -> str:
        text = re.sub(r"^---[\s\S]*?---\n", "", text)
        text = re.sub(r"```[\s\S]*?```", "", text)
        text = re.sub(r"`[^`]+`", "", text)
        text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
        text = re.sub(r"\[[^\]]+\]\([^)]+\)", r"\1", text)
        text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
        text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
        text = re.sub(r"\*(.+?)\*", r"\1", text)
        text = re.sub(r"^\s*[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)
        text = re.sub(r"\|.+\|", "", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()

    def _path_to_url(self, doc_path: str) -> str:
        return f"/{doc_path}"

    async def _build_index(self):
        if self.use_openai:
            try:
                from openai import OpenAI

                client = OpenAI()
                embeddings = []
                for chunk in tqdm(self.chunks, desc="Generando embeddings (OpenAI)"):
                    response = client.embeddings.create(
                        model="text-embedding-3-small",
                        input=chunk["content"],
                    )
                    embeddings.append(response.data[0].embedding)
                self.chunk_embeddings = np.array(embeddings).astype("float32")
            except Exception as e:
                print(f"OpenAI no disponible, usando modelo local: {e}")
                self.use_openai = False

        if not self.use_openai:
            model_name = os.getenv(
                "EMBEDDING_MODEL", "paraphrase-multilingual-MiniLM-L12-v2"
            )
            self.model = SentenceTransformer(model_name)
            texts = [chunk["content"] for chunk in self.chunks]
            embeddings = self.model.encode(texts, show_progress_bar=True)
            self.chunk_embeddings = embeddings.astype("float32")

        faiss.normalize_L2(self.chunk_embeddings)
        dimension = self.chunk_embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(self.chunk_embeddings)

    async def search(self, query: str, top_k: int = 5) -> list[dict]:
        if self.index is None or self.model is None:
            raise RuntimeError("Índice no inicializado")

        if self.use_openai:
            from openai import OpenAI

            client = OpenAI()
            response = client.embeddings.create(
                model="text-embedding-3-small",
                input=query,
            )
            query_embedding = np.array([response.data[0].embedding]).astype("float32")
        else:
            query_embedding = self.model.encode([query]).astype("float32")

        faiss.normalize_L2(query_embedding)
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx < len(self.chunks):
                chunk = self.chunks[idx].copy()
                chunk["score"] = float(dist)
                results.append(chunk)

        return results

    async def answer_question(
        self, question: str, top_k: int = 3, include_raw: bool = False
    ) -> dict:
        context_chunks = await self.search(question, top_k=top_k)

        if not context_chunks:
            return {
                "answer": "No he encontrado información relevante para tu pregunta en la base de conocimiento.",
                "sources": [],
            }

        context = "\n\n---\n\n".join(
            [f"[Fuente: {c['source']}]\n{c['content']}" for c in context_chunks]
        )

        if self.use_openai:
            from openai import OpenAI

            client = OpenAI()
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Eres un asistente especializado en restauración. "
                            "Responde en español, de forma clara y práctica. "
                            "Cita las fuentes cuando sea posible. "
                            "Si no tienes información suficiente, indícalo."
                        ),
                    },
                    {
                        "role": "user",
                        "content": f"Pregunta: {question}\n\nContexto:\n{context}",
                    },
                ],
                temperature=0.3,
                max_tokens=600,
            )
            answer = response.choices[0].message.content
        else:
            top_chunk = context_chunks[0]
            snippet = top_chunk["content"][:600]
            answer = (
                f"Basándome en la documentación, esto es lo que puedo responder:\n\n"
                f"{snippet}...\n\n"
                f"[Fuente: {top_chunk['source']}]"
            )

        sources = [
            {
                "content": c["content"][:300] + "..."
                if len(c["content"]) > 300
                else c["content"],
                "source": c["source"],
                "score": c["score"],
                "url": c["url"],
            }
            for c in context_chunks
        ]

        return {
            "answer": answer,
            "sources": sources,
        }
