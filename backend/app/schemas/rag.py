from pydantic import BaseModel, Field


class RAGRequest(BaseModel):
    document_id: str = Field(
        ...,
        description="ID of the processed document",
        examples=["a9cc48a6-c21a-43ee-b146-95898868fbd8"]
    )

    question: str = Field(
        ...,
        min_length=3,
        description="Question to answer using the document",
        examples=["What skills are required for an AI Engineer?"]
    )

    limit: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Number of relevant chunks to retrieve",
        examples=[3]
    )


class RAGSource(BaseModel):
    source_file: str = Field(
        ...,
        description="Original uploaded PDF filename",
        examples=["Guide.pdf"]
    )

    chunk_id: int = Field(
        ...,
        description="ID of the retrieved document chunk",
        examples=[1]
    )

    similarity_score: float = Field(
        ...,
        description="Semantic similarity score for the retrieved chunk",
        examples=[0.73]
    )

    excerpt: str = Field(
        ...,
        description="Short excerpt from the retrieved source chunk",
        examples=[
            "An AI Engineer designs, develops, deploys, and maintains AI systems."
        ]
    )


class RAGResponse(BaseModel):
    document_id: str = Field(
        ...,
        description="ID of the document used to generate the answer"
    )

    question: str = Field(
        ...,
        description="Question submitted by the user"
    )

    answer: str = Field(
        ...,
        description="Grounded AI-generated answer"
    )

    sources: list[RAGSource] = Field(
        ...,
        description="Retrieved document sources used to generate the answer"
    )