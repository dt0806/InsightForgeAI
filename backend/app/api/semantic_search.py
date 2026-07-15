from fastapi import APIRouter, HTTPException

from app.schemas.semantic_search import (
    SemanticSearchRequest,
    SemanticSearchResponse,
)
from app.services.semantic_search_service import semantic_search


router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.post(
    "/semantic",
    response_model=SemanticSearchResponse,
    summary="Search a document using semantic similarity",
    description=(
        "Creates an embedding for the user question, compares it with "
        "stored document embeddings, and returns the most relevant chunks."
    ),
)
def search_semantically(request: SemanticSearchRequest):
    try:
        matches = semantic_search(
            document_id=request.document_id,
            question=request.question,
            limit=request.limit
        )

    except FileNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        ) from error

    except ValueError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        ) from error

    return {
        "document_id": request.document_id,
        "question": request.question,
        "match_count": len(matches),
        "matches": matches
    }