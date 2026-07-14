from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest
from app.services.search_service import semantic_search


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("")
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
        "match_count": len(matches),
        "matches": matches
    }