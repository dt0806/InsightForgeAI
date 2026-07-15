from fastapi import APIRouter, HTTPException

from app.schemas.rag import RAGRequest, RAGResponse
from app.services.rag_service import answer_question


router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)


@router.post(
    "/answer",
    response_model=RAGResponse,
    summary="Generate a grounded answer from a document",
    description=(
        "Retrieves the most relevant document chunks using semantic search "
        "and generates an answer using only the retrieved context."
    ),
)
def generate_rag_answer(request: RAGRequest):
    try:
        result = answer_question(
            document_id=request.document_id,
            question=request.question,
            limit=request.limit,
        )

    except FileNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        ) from error

    except RuntimeError as error:
        raise HTTPException(
            status_code=503,
            detail=str(error),
        ) from error

    except ValueError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        ) from error

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=(
                f"Unexpected RAG error: "
                f"{type(error).__name__}: {error}"
            ),
        ) from error

    return {
        "document_id": request.document_id,
        "question": request.question,
        "answer": result["answer"],
        "sources": result["sources"],
    }