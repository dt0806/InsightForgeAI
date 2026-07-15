import json

import numpy as np

from app.services import storage_service


def test_save_chunk_records_creates_json_file(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(
        storage_service,
        "PROCESSED_DIR",
        tmp_path,
    )

    records = [
        {
            "chunk_id": 1,
            "document_id": "test-document",
            "source_file": "Guide.pdf",
            "content": "Sample chunk text.",
            "character_count": 18,
        }
    ]

    output_path = storage_service.save_chunk_records(
        document_id="test-document",
        records=records,
    )

    assert output_path.exists()
    assert output_path.name == "test-document.json"

    saved_records = json.loads(
        output_path.read_text(encoding="utf-8")
    )

    assert saved_records == records


def test_save_embeddings_creates_numpy_file(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(
        storage_service,
        "PROCESSED_DIR",
        tmp_path,
    )

    embeddings = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
        ],
        dtype=np.float32,
    )

    output_path = storage_service.save_embeddings(
        document_id="test-document",
        embeddings=embeddings,
    )

    assert output_path.exists()
    assert output_path.name == "test-document.npy"

    saved_embeddings = np.load(output_path)

    assert np.array_equal(
        saved_embeddings,
        embeddings,
    )