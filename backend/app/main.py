from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.documents import router as documents_router
from app.api.upload import router as upload_router
from app.api.health import router as health_router
from app.api.rag import router as rag_router
from app.api.semantic_search import router as semantic_search_router


app = FastAPI(
    title="InsightForgeAI API",
    description=(
        "Enterprise AI knowledge and document intelligence platform "
        "with PDF ingestion, semantic search, and grounded RAG answers."
    ),
    version="1.0.0"
)


@app.get("/",
    summary="API welcome endpoint",
    description="Returns a basic confirmation that the API is running.",
)
def root():
    return {
        "message": "Welcome to InsightForgeAI API",
        "status": "running"
    }


app.include_router(health_router)
app.include_router(upload_router)
app.include_router(documents_router)
app.include_router(chat_router)
app.include_router(semantic_search_router)
app.include_router(rag_router)