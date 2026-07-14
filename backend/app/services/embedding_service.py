from functools import lru_cache

import numpy as np
from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def get_embedding_model() -> SentenceTransformer:
    """
    Load and cache the embedding model.

    The model is loaded only once while the application is running.
    """

    return SentenceTransformer(MODEL_NAME)


def create_embeddings(texts: list[str]) -> np.ndarray:
    """
    Convert text values into normalized embedding vectors.
    """

    if not texts:
        return np.empty((0, 0), dtype=np.float32)

    model = get_embedding_model()

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=False
    )

    return np.asarray(embeddings, dtype=np.float32)


def create_query_embedding(question: str) -> np.ndarray:
    """
    Convert one user question into a normalized embedding vector.
    """

    model = get_embedding_model()

    embedding = model.encode(
        [question],
        normalize_embeddings=True,
        show_progress_bar=False
    )

    return np.asarray(embedding[0], dtype=np.float32)