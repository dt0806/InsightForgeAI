def generate_answer(
    question: str,
    context: str
) -> str:
    """
    Generate an answer from retrieved document context.

    This temporary implementation validates the complete RAG workflow.
    It will later be replaced with an external or local LLM call.
    """

    if not context.strip():
        return (
            "The document does not contain enough information "
            "to answer this question."
        )

    return (
        "Based on the retrieved document context:\n\n"
        f"{context[:1500]}"
    )