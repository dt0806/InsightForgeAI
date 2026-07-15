import json

import numpy as np
import pytest

from app.services import semantic_search_service


def test_semantic_search_returns_best_match_first(
    tmp_path,
    monkeypatch,
):
    document_id = "test-document"

    records = [
        {
            "chunk_id": 1,
            "document_id": document_id,
            "source_file": "Guide.pdf",
            "content": "Python and SQL are important data engineering skills.",
            "character_count": 55,
        },
        {
            "chunk_id": 2,
            "document_id": document_id,
            "source_file": "Guide.pdf",
            "content": "Cooking recipes and kitchen equipment.",
            "character_count": 38,
        },
    ]

    metadata_path = tmp_path / f"{document_id}.json"
    embeddings_path = tmp_path / f"{document_id}.npy"

    metadata_path.write_text(
        json.dumps(records),
        encoding="utf-8",
    )

    document_embeddings = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
        ],
        dtype=np.float32,
    )

    np.save(
        embeddings_path,
        document_embeddings,
    )

    monkeypatch.setattr(
        semantic_search_service,
        "PROCESSED_DIR",
        tmp_path,
    )

    monkeypatch.setattr(
        semantic_search_service,
        "create_query_embedding",
        lambda question: np.array(
            [1.0, 0.0],
            dtype=np.float32,
        ),
    )

    matches = semantic_search_service.semantic_search(
        document_id=document_id,
        question="What skills are needed for data engineering?",
        limit=2,
    )

    assert len(matches) == 2
    assert matches[0]["chunk_id"] == 1
    assert matches[0]["similarity_score"] == 1.0
    assert matches[0]["source_file"] == "Guide.pdf"
    assert matches[0]["document_id"] == document_id


def test_semantic_search_raises_error_when_document_is_missing(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(
        semantic_search_service,
        "PROCESSED_DIR",
        tmp_path,
    )

    with pytest.raises(
        FileNotFoundError,
        match="Processed document 'missing-document' was not found.",
    ):
        semantic_search_service.semantic_search(
            document_id="missing-document",
            question="What is this document about?",
            limit=3,
        )


def test_semantic_search_raises_error_for_mismatched_counts(
    tmp_path,
    monkeypatch,
):
    document_id = "mismatched-document"

    records = [
        {
            "chunk_id": 1,
            "document_id": document_id,
            "source_file": "Guide.pdf",
            "content": "First chunk",
            "character_count": 11,
        }
    ]

    metadata_path = tmp_path / f"{document_id}.json"
    embeddings_path = tmp_path / f"{document_id}.npy"

    metadata_path.write_text(
        json.dumps(records),
        encoding="utf-8",
    )

    document_embeddings = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
        ],
        dtype=np.float32,
    )

    np.save(
        embeddings_path,
        document_embeddings,
    )

    monkeypatch.setattr(
        semantic_search_service,
        "PROCESSED_DIR",
        tmp_path,
    )

    with pytest.raises(
        ValueError,
        match="Chunk metadata and embedding counts do not match.",
    ):
        semantic_search_service.semantic_search(
            document_id=document_id,
            question="Test question",
            limit=3,
        )