from pydantic import BaseModel, Field


class SemanticSearchRequest(BaseModel):
    document_id: str = Field(
        ...,
        description="ID of the processed document",
        examples=["a9cc48a6-c21a-43ee-b146-95898868fbd8"],
    )

    question: str = Field(
        ...,
        min_length=3,
        description="Question used to search the document semantically",
        examples=["What skills are required for an AI Engineer?"],
    )

    limit: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Maximum number of relevant chunks to return",
        examples=[3],
    )


class SemanticSearchMatch(BaseModel):
    source_file: str = Field(
        ...,
        description="Original uploaded PDF filename",
        examples=["Guide.pdf"],
    )

    chunk_id: int = Field(
        ...,
        description="ID of the matched document chunk",
        examples=[1],
    )

    document_id: str = Field(
        ...,
        description="ID of the searched document",
        examples=["a9cc48a6-c21a-43ee-b146-95898868fbd8"],
    )

    content: str = Field(
        ...,
        description="Text content of the matched chunk",
        examples=[
            "An AI Engineer designs, develops, deploys, "
            "and maintains artificial intelligence systems."
        ],
    )

    similarity_score: float = Field(
        ...,
        description="Semantic similarity score for this match",
        examples=[0.73],
    )


class SemanticSearchResponse(BaseModel):
    document_id: str = Field(
        ...,
        description="ID of the searched document",
    )

    question: str = Field(
        ...,
        description="Question submitted by the user",
    )

    match_count: int = Field(
        ...,
        description="Number of semantic matches returned",
        examples=[3],
    )

    matches: list[SemanticSearchMatch] = Field(
        ...,
        description="Ranked semantic-search results",
    )