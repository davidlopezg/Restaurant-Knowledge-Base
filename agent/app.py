"""Agente RAG para la Knowledge Base de Restaurantes.

Backend FastAPI con búsqueda semántica y generación de respuestas.
Uso opcional con OpenAI o embeddings locales (sentence-transformers).
"""

import os
import sys
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

sys.path.append(str(Path(__file__).parent))

from search import KnowledgeBase

app = FastAPI(
    title="Asistente KB Restaurantes",
    description="API del asistente conversacional para la base de conocimiento de restauración.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

kb: Optional[KnowledgeBase] = None


class QuestionRequest(BaseModel):
    question: str
    top_k: int = 3
    include_raw: bool = False


class SourceDocument(BaseModel):
    content: str
    source: str
    score: float
    url: Optional[str] = None


class AnswerResponse(BaseModel):
    answer: str
    sources: list[SourceDocument]
    model: str


@app.on_event("startup")
async def startup_event():
    global kb
    docs_path = Path(__file__).parent.parent / "docs"
    kb = KnowledgeBase(docs_dir=str(docs_path))
    await kb.initialize()
    print(f"Knowledge Base inicializada con {len(kb.chunks)} fragmentos.")


@app.get("/", response_class=HTMLResponse)
async def root():
    template_path = Path(__file__).parent / "templates" / "chat.html"
    if template_path.exists():
        return template_path.read_text(encoding="utf-8")
    raise HTTPException(status_code=404, detail="Plantilla no encontrada")


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "model": os.getenv("OPENAI_API_KEY", "local-embeddings"),
        "chunks": len(kb.chunks) if kb else 0,
    }


@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    """Recibe una pregunta y devuelve la respuesta con citas."""
    if not kb:
        raise HTTPException(status_code=503, detail="Knowledge Base no inicializada")

    try:
        result = await kb.answer_question(
            question=request.question,
            top_k=request.top_k,
            include_raw=request.include_raw,
        )
        return AnswerResponse(
            answer=result["answer"],
            sources=result["sources"],
            model=os.getenv("OPENAI_API_KEY", "local-embeddings"),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search")
async def search_docs(q: str, top_k: int = 5):
    """Búsqueda simple de fragmentos relevantes."""
    if not kb:
        raise HTTPException(status_code=503, detail="Knowledge Base no inicializada")

    results = await kb.search(q, top_k=top_k)
    return {"results": results}


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
