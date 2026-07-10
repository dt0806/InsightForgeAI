import json
import re
from pathlib import Path
from typing import Any


PROCESSED_DIR = Path("processed")

STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "how",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "what",
    "when",
    "where",
    "which",
    "who",
    "why",
    "with"
}


def extract_keywords(question: str) -> set[str]:
    """
    Convert a question into lowercase searchable keywords.
    """

    words = re.findall(r"\b[a-zA-Z0-9]+\b", question.lower())

    return {
        word
        for word in words
        if word not in STOP_WORDS and len(word) > 1
    }


def search_document_chunks(
    document_id: str,
    question: str,
    limit: int = 3
) -> list[dict[str, Any]]:
    """
    Find document chunks containing the question's keywords.
    """

    document_path = PROCESSED_DIR / f"{document_id}.json"

    if not document_path.exists():
        raise FileNotFoundError(
            f"Processed document '{document_id}' was not found."
        )

    with open(document_path, "r", encoding="utf-8") as input_file:
        records = json.load(input_file)

    keywords = extract_keywords(question)

    scored_records = []

    for record in records:
        content = record.get("content", "")
        searchable_content = content.lower()

        score = sum(
            searchable_content.count(keyword)
            for keyword in keywords
        )

        if score > 0:
            scored_records.append(
                {
                    "score": score,
                    "chunk_id": record["chunk_id"],
                    "document_id": record["document_id"],
                    "source_file": record["source_file"],
                    "content": content,
                    "character_count": record["character_count"]
                }
            )

    scored_records.sort(
        key=lambda record: record["score"],
        reverse=True
    )

    return scored_records[:limit]