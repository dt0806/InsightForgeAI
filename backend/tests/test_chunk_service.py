from app.services.chunk_service import create_chunk_records


def test_create_chunk_records_builds_correct_records():
    chunks = [
        "First chunk text.",
        "Second chunk text.",
    ]

    records = create_chunk_records(
        chunks=chunks,
        document_id="test-document",
        source_file="Guide.pdf",
    )

    assert len(records) == 2

    assert records[0] == {
        "chunk_id": 1,
        "document_id": "test-document",
        "source_file": "Guide.pdf",
        "content": "First chunk text.",
        "character_count": len("First chunk text."),
    }

    assert records[1] == {
        "chunk_id": 2,
        "document_id": "test-document",
        "source_file": "Guide.pdf",
        "content": "Second chunk text.",
        "character_count": len("Second chunk text."),
    }


def test_create_chunk_records_returns_empty_list_for_no_chunks():
    records = create_chunk_records(
        chunks=[],
        document_id="test-document",
        source_file="Guide.pdf",
    )

    assert records == []