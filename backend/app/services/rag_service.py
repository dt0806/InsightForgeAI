from typing import Any

from app.services.llm_service import generate_answer
from app.services.semantic_search_service import semantic_search


def answer_question(
    document_id: str,
    question: str,
    limit: int = 3
) -> dict[str, Any]:
    """
    Retrieve relevant document chunks and generate a grounded answer.
    """

    matches = semantic_search(
        document_id=document_id,
        question=question,
        limit=limit
    )

    if not matches:
        return {
            "answer": (
                "The document does not contain enough information "
                "to answer this question."
            ),
            "sources": []
        }

    context_sections = []

    for match in matches:
        context_sections.append(
            (
                f"Source file: {match['source_file']}\n"
                f"Chunk ID: {match['chunk_id']}\n"
                f"Content: {match['content']}"
            )
        )

    context = "\n\n---\n\n".join(context_sections)

    answer = generate_answer(
        question=question,
        context=context
    )

    sources = []

    for match in matches:
        sources.append(
            {
                "source_file": match["source_file"],
                "chunk_id": match["chunk_id"],
                "similarity_score": match["similarity_score"],
                "excerpt": match["content"][:300]
            }
        )

    return {
        "answer": answer,
        "sources": sources
    }