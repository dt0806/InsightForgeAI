import json
from pathlib import Path
from typing import Any

import numpy as np

from app.services.embedding_service import create_query_embedding


PROCESSED_DIR = Path("processed")


def semantic_search(
    document_id: str,
    question: str,
    limit: int = 3
) -> list[dict[str, Any]]:
    """
    Return the document chunks most similar to a user question.
    """

    metadata_path = PROCESSED_DIR / f"{document_id}.json"
    embeddings_path = PROCESSED_DIR / f"{document_id}.npy"

    if not metadata_path.exists():
        raise FileNotFoundError(
            f"Processed document '{document_id}' was not found."
        )

    if not embeddings_path.exists():
        raise FileNotFoundError(
            f"Embeddings for document '{document_id}' were not found. "
            "Upload the document again to generate embeddings."
        )

    with open(metadata_path, "r", encoding="utf-8") as input_file:
        records = json.load(input_file)

    document_embeddings = np.load(embeddings_path)

    if len(records) != len(document_embeddings):
        raise ValueError(
            "Chunk metadata and embedding counts do not match."
        )

    query_embedding = create_query_embedding(question)

    similarity_scores = document_embeddings @ query_embedding

    ranked_indices = np.argsort(similarity_scores)[::-1][:limit]

    matches = []

    for index in ranked_indices:
        record = records[int(index)]

        matches.append(
            {
                "similarity_score": round(
                    float(similarity_scores[index]),
                    4
                ),
                "chunk_id": record["chunk_id"],
                "document_id": record["document_id"],
                "source_file": record["source_file"],
                "content": record["content"],
                "character_count": record["character_count"]
            }
        )

    return matches