from typing import Any


def create_chunk_records(
    chunks: list[str],
    document_id: str,
    source_file: str
) -> list[dict[str, Any]]:
    """
    Convert plain text chunks into structured chunk records.
    """

    records = []

    for index, chunk in enumerate(chunks, start=1):
        records.append(
            {
                "chunk_id": index,
                "document_id": document_id,
                "source_file": source_file,
                "content": chunk,
                "character_count": len(chunk)
            }
        )

    return records