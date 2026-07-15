from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    document_id: str = Field(
        ...,
        description="ID of the processed document",
        examples=["a9cc48a6-c21a-43ee-b146-95898868fbd8"],
    )

    question: str = Field(
        ...,
        min_length=3,
        description="Question to search within the document",
        examples=["What skills are required for an AI Engineer?"],
    )

    limit: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Maximum number of semantic matches to return",
        examples=[3],
    )


class ChatMatch(BaseModel):
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
    )

    content: str = Field(
        ...,
        description="Text content of the matched document chunk",
    )

    similarity_score: float = Field(
        ...,
        description="Semantic similarity score for this result",
        examples=[0.73],
    )


class ChatResponse(BaseModel):
    document_id: str = Field(
        ...,
        description="ID of the searched document",
    )

    question: str = Field(
        ...,
        description="Question submitted by the user",
    )

    retrieval_method: str = Field(
        ...,
        description="Retrieval strategy used by the chat endpoint",
        examples=["semantic"],
    )

    match_count: int = Field(
        ...,
        description="Number of matches returned",
        examples=[3],
    )

    matches: list[ChatMatch] = Field(
        ...,
        description="Ranked semantic-search matches",
    )