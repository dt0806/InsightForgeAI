import json
from pathlib import Path

from fastapi import APIRouter

router = APIRouter()

PROCESSED_DIR = Path("processed")


@router.get("/documents")
def list_documents():
    documents = []

    if not PROCESSED_DIR.exists():
        return {"documents": documents}

    for json_file in PROCESSED_DIR.glob("*.json"):
        with open(json_file, "r", encoding="utf-8") as file:
            records = json.load(file)

        if not records:
            continue

        first_record = records[0]

        documents.append(
            {
                "document_id": first_record["document_id"],
                "source_file": first_record["source_file"],
                "chunk_count": len(records)
            }
        )

    return {
        "documents": documents,
        "total_documents": len(documents)
    }