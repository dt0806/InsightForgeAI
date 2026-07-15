from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.semantic_search_service import semantic_search


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "",
    response_model=ChatResponse,
    summary="Search a document through the chat endpoint",
    description=(
        "Uses semantic retrieval to find the most relevant document chunks "
        "for the submitted question."
    ),
)
def search_document(request: ChatRequest):
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
        "retrieval_method": "semantic",
        "match_count": len(matches),
        "matches": matches
    }