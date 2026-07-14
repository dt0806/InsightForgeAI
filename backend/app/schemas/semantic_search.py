from pydantic import BaseModel, Field


class SemanticSearchRequest(BaseModel):
    document_id: str = Field(
        ...,
        description="Document ID"
    )

    question: str = Field(
        ...,
        min_length=3
    )

    limit: int = Field(
        default=3,
        ge=1,
        le=10
    )