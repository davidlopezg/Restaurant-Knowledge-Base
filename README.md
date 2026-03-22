# Knowledge Base para Restaurantes

Base de conocimiento colaborativa en código abierto para profesionales de la restauración. Manuales operativos, guías de sistemas, habilidades prácticas y un asistente conversacional que responde preguntas sobre todos los contenidos.

---

## Visión del proyecto

La industria de la restauración necesita documentación operativa rigurosa, accesible y en constante evolución. Este proyecto ofrece:

- **Manuales operativos** detallados para apertura, operaciones diarias y finanzas.
- **Sistemas de gestión** con plantillas y metodologías probadas (control de costes, inventario, ingeniería de menú).
- **Skills prácticas** para la gestión del equipo, atención al cliente y resolución de conflictos.
- **Asistente IA** que responde preguntas en lenguaje natural sobre cualquier contenido de la base de conocimiento.

Todo el contenido es código abierto, editable por la comunidad y adaptable a cualquier concepto de restauración.

---

## Tecnologías

| Componente | Tecnología |
|---|---|
| Documentación | MkDocs + Material for MkDocs |
| Búsqueda estática | lunr.js (frontend) |
| Asistente IA | Python + FastAPI + RAG |
| Embeddings | sentence-transformers (local) o OpenAI |
| Despliegue | GitHub Pages |
| CI/CD | GitHub Actions |

---

## Despliegue rápido

### 1. Publicar en GitHub Pages

1. Crea un repositorio en GitHub (ej: `restaurant-knowledge-base`).
2. Sube todo el contenido de este proyecto al repositorio.
3. Ve a **Settings → Pages → Source** y selecciona la rama `main` con la carpeta `/ (root)`.
4. En **Build and deployment → Source**, selecciona **GitHub Actions**.
5. Haz un push a `main`. El workflow `.github/workflows/ci.yml` compilará MkDocs y desplegará automáticamente.

Tu web estará disponible en:

```
https://TU_USUARIO.github.io/restaurant-knowledge-base/
```

> **Nota:** Si usas un nombre de repositorio diferente, actualiza `site_url` en `mkdocs.yml` y los enlaces en `README.md`.

### 2. Verificar el despliegue

1. Ve a la pestaña **Actions** de tu repositorio.
2. Comprueba que el workflow "Build and Deploy to GitHub Pages" se ejecuta correctamente.
3. Accede a tu URL de GitHub Pages una vez completado.

---

## Desarrollo local

### Documentación (MkDocs)

```bash
# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .\.venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Servidor de desarrollo con recarga automática
mkdocs serve
```

La web estará disponible en `http://localhost:8000`.

### Asistente IA (backend opcional)

```bash
# Crear entorno virtual para el agente
python -m venv agent-venv
source agent-venv/bin/activate  # Linux/macOS
# agent-venv\Scripts\activate   # Windows

# Instalar dependencias del agente
pip install -r requirements-agent.txt

# Ejecutar el servidor
cd agent
python app.py
```

El asistente estará disponible en `http://localhost:8000` (reemplaza la interfaz web de MkDocs).

### Variables de entorno (opcional)

```bash
# Para usar OpenAI en lugar de embeddings locales (requiere API key)
export OPENAI_API_KEY=sk-tu-api-key-aqui

# Modelo de embeddings local (por defecto: paraphrase-multilingual-MiniLM-L12-v2)
export EMBEDDING_MODEL=all-MiniLM-L6-v2

# Puerto del servidor (por defecto: 8000)
export PORT=8000
```

---

## Estructura del proyecto

```
restaurant-knowledge-base/
├── docs/                       # Contenido markdown
│   ├── index.md               # Página principal
│   ├── manuales/               # Manuales operativos
│   ├── sistemas/               # Sistemas de gestión
│   ├── skills/                 # Habilidades prácticas
│   ├── agentes/                # FAQ del asistente
│   ├── chat.html               # Interfaz del asistente
│   └── stylesheets/extra.css   # Estilos personalizados
├── agent/                      # Backend Python (opcional)
│   ├── app.py                  # Servidor FastAPI
│   ├── search.py               # Módulo RAG
│   └── templates/chat.html     # Plantilla del asistente
├── assets/                     # Recursos estáticos
│   ├── images/
│   └── templates/             # Plantillas descargables
├── .github/workflows/ci.yml   # CI/CD para GitHub Pages
├── mkdocs.yml                 # Configuración de MkDocs
├── requirements.txt           # Dependencias MkDocs
├── requirements-agent.txt     # Dependencias agente IA
├── plugin.py                  # Hook de MkDocs
├── LICENSE                    # Licencia MIT
└── README.md                  # Este archivo
```

---

## Contribución

Este proyecto es código abierto y welcome las contribuciones de la comunidad de restauración.

**Para contribuir:**

1. Haz un fork del repositorio.
2. Crea una rama para tu feature o corrección: `git checkout -b mi-correccion`.
3. Realiza tus cambios y documenta claramente qué añades o modificas.
4. Envía un pull request con una descripción de los cambios.

**Ideas para contribuir:**

- Añadir nuevos manuales o secciones específicas (carta de vinos, coctelería, sostenibilidad).
- Traducir el contenido a otros idiomas.
- Mejorar las respuestas del asistente con más ejemplos y casos prácticos.
- Añadir plantillas de Excel o herramientas descargables.
- Reportar errores o inconsistencias en el contenido.

---

## Servicios de personalización

¿Necesitas adaptar esta base de conocimiento a tu restaurante, integrar el asistente IA con tu propio conocimiento, o formar a tu equipo? Ofrezco servicios de:

- **Personalización de manuales** para tu concepto, formato y necesidades específicas.
- **Implantación de sistemas** de control de costes y reporting financiero.
- **Desarrollo de agentes IA** con tu propio conocimiento, personalidad de marca e integraciones.
- **Formación presencial** para equipos de sala y cocina.

[Solicitar personalización](mailto:david@example.com)

---

## Licencia

Este proyecto está bajo licencia **MIT**. Puedes usar, modificar y distribuir el contenido libremente, siempre que menciones la atribución y uses la misma licencia.

Ver archivo [LICENSE](LICENSE) para los detalles completos.

---

*Creado con el objetivo de elevar el nivel de la industria de la restauración a través del conocimiento compartido.*
