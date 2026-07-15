from pydantic import BaseModel, Field


class DocumentSummary(BaseModel):
    document_id: str = Field(
        ...,
        description="Unique ID of the processed document",
        examples=["a9cc48a6-c21a-43ee-b146-95898868fbd8"],
    )

    source_file: str = Field(
        ...,
        description="Original uploaded PDF filename",
        examples=["Guide.pdf"],
    )

    chunk_count: int = Field(
        ...,
        description="Number of chunks created for the document",
        examples=[5],
    )


class DocumentListResponse(BaseModel):
    documents: list[DocumentSummary] = Field(
        ...,
        description="List of processed documents",
    )