from pydantic import BaseModel, Field


class RAGRequest(BaseModel):
    document_id: str = Field(
        ...,
        description="ID of the processed document"
    )

    question: str = Field(
        ...,
        min_length=3,
        description="Question to answer using the document"
    )

    limit: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Number of relevant chunks to retrieve"
    )