from fastapi.testclient import TestClient

from app.api import rag as rag_api
from app.main import app


client = TestClient(app)


def test_rag_answer_endpoint_returns_answer_and_sources(
    monkeypatch,
):
    fake_result = {
        "answer": (
            "AI Engineers need Python, machine learning, "
            "cloud, API, Docker, and MLOps skills."
        ),
        "sources": [
            {
                "source_file": "Guide.pdf",
                "chunk_id": 1,
                "similarity_score": 0.91,
                "excerpt": (
                    "AI Engineers use Python, machine learning, "
                    "Docker, and cloud platforms."
                ),
            }
        ],
    }

    monkeypatch.setattr(
        rag_api,
        "answer_question",
        lambda document_id, question, limit: fake_result,
    )

    response = client.post(
        "/rag/answer",
        json={
            "document_id": "test-document",
            "question": (
                "What skills are required for an AI Engineer?"
            ),
            "limit": 3,
        },
    )

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["document_id"] == "test-document"
    assert response_data["question"] == (
        "What skills are required for an AI Engineer?"
    )

    assert response_data["answer"] == fake_result["answer"]
    assert response_data["sources"] == fake_result["sources"]


def test_rag_answer_endpoint_returns_404_for_missing_document(
    monkeypatch,
):
    def raise_missing_document(
        document_id,
        question,
        limit,
    ):
        raise FileNotFoundError(
            "Processed document 'missing-document' was not found."
        )

    monkeypatch.setattr(
        rag_api,
        "answer_question",
        raise_missing_document,
    )

    response = client.post(
        "/rag/answer",
        json={
            "document_id": "missing-document",
            "question": "What is this document about?",
            "limit": 3,
        },
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": (
            "Processed document 'missing-document' "
            "was not found."
        )
    }