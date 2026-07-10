def split_text_into_chunks(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200
) -> list[str]:
    """
    Split text into overlapping character-based chunks.

    Args:
        text: Complete extracted document text.
        chunk_size: Maximum number of characters in each chunk.
        overlap: Number of characters repeated between adjacent chunks.

    Returns:
        A list of text chunks.
    """

    cleaned_text = text.strip()

    if not cleaned_text:
        return []

    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size.")

    chunks = []
    start = 0

    while start < len(cleaned_text):
        end = start + chunk_size
        chunk = cleaned_text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks