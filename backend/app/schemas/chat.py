from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    document_id: str = Field(
        ...,
        description="ID of the processed document"
    )

    question: str = Field(
        ...,
        min_length=3,
        description="Question about the document"
    )

    limit: int = Field(
        default=3,
        ge=1,
        le=10
    )