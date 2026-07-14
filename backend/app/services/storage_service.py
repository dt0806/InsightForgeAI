import json

from pathlib import Path
from typing import Any

import numpy as np

PROCESSED_DIR = Path("processed")
PROCESSED_DIR.mkdir(exist_ok=True)


def save_chunk_records(
    document_id: str,
    records: list[dict[str, Any]]
) -> Path:
    """
    Save processed document chunks as a JSON file.
    """

    output_path = PROCESSED_DIR / f"{document_id}.json"

    with open(output_path, "w", encoding="utf-8") as output_file:
        json.dump(records, output_file, ensure_ascii=False, indent=2)

    return output_path


def save_embeddings(
    document_id: str,
    embeddings: np.ndarray
) -> Path:
    """
    Save document embedding vectors as a NumPy file.
    """

    output_path = PROCESSED_DIR / f"{document_id}.npy"

    np.save(output_path, embeddings)

    return output_path