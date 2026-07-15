from app.services import rag_service


def test_answer_question_returns_answer_and_sources(
    monkeypatch,
):
    fake_matches = [
        {
            "source_file": "Guide.pdf",
            "chunk_id": 1,
            "similarity_score": 0.91,
            "content": (
                "AI Engineers use Python, machine learning, "
                "Docker, and cloud platforms."
            ),
        },
        {
            "source_file": "Guide.pdf",
            "chunk_id": 2,
            "similarity_score": 0.82,
            "content": (
                "They also work with APIs, MLOps, monitoring, "
                "and deployment tools."
            ),
        },
    ]

    monkeypatch.setattr(
        rag_service,
        "semantic_search",
        lambda document_id, question, limit: fake_matches,
    )

    monkeypatch.setattr(
        rag_service,
        "generate_answer",
        lambda question, context: (
            "AI Engineers need Python, machine learning, "
            "cloud, APIs, Docker, and MLOps skills."
        ),
    )

    result = rag_service.answer_question(
        document_id="test-document",
        question="What skills are required for an AI Engineer?",
        limit=2,
    )

    assert result["answer"] == (
        "AI Engineers need Python, machine learning, "
        "cloud, APIs, Docker, and MLOps skills."
    )

    assert len(result["sources"]) == 2

    assert result["sources"][0] == {
        "source_file": "Guide.pdf",
        "chunk_id": 1,
        "similarity_score": 0.91,
        "excerpt": (
            "AI Engineers use Python, machine learning, "
            "Docker, and cloud platforms."
        ),
    }


def test_answer_question_returns_fallback_when_no_matches(
    monkeypatch,
):
    monkeypatch.setattr(
        rag_service,
        "semantic_search",
        lambda document_id, question, limit: [],
    )

    result = rag_service.answer_question(
        document_id="test-document",
        question="What is the vacation policy?",
        limit=3,
    )

    assert result == {
        "answer": (
            "The document does not contain enough information "
            "to answer this question."
        ),
        "sources": [],
    }