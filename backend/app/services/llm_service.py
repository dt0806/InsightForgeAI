from openai import OpenAI

from app.config.settings import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
    validate_llm_settings,
)


SYSTEM_PROMPT = """
You are a document question-answering assistant.

Answer only from the supplied document context.

Rules:
1. Do not invent facts.
2. If the context does not contain enough information, say:
   "The document does not contain enough information to answer this question."
3. Keep the answer clear and concise.
4. Do not use outside knowledge.
"""


def generate_answer(
    question: str,
    context: str,
) -> str:
    if not context.strip():
        return (
            "The document does not contain enough information "
            "to answer this question."
        )

    validate_llm_settings()

    client = OpenAI(api_key=OPENAI_API_KEY)

    user_prompt = f"""
Document context:

{context}

Question:

{question}

Answer using only the document context.
"""

    response = client.responses.create(
        model=OPENAI_MODEL,
        instructions=SYSTEM_PROMPT,
        input=user_prompt,
    )

    answer = " ".join(
        response.output_text.split()
    )

    if not answer:
        return (
            "The document does not contain enough information "
            "to answer this question."
        )

    return answer