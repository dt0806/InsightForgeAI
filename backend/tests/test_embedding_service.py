import numpy as np

from app.services import embedding_service


class FakeEmbeddingModel:
    def encode(
        self,
        texts,
        normalize_embeddings=True,
        show_progress_bar=False,
    ):
        if len(texts) == 1:
            return np.array(
                [[0.6, 0.8]],
                dtype=np.float32,
            )

        return np.array(
            [
                [1.0, 0.0],
                [0.0, 1.0],
            ],
            dtype=np.float32,
        )


def test_create_embeddings_returns_expected_shape(
    monkeypatch,
):
    monkeypatch.setattr(
        embedding_service,
        "get_embedding_model",
        lambda: FakeEmbeddingModel(),
    )

    embeddings = embedding_service.create_embeddings(
        [
            "Python and SQL",
            "Docker and Kubernetes",
        ]
    )

    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape == (2, 2)
    assert embeddings.dtype == np.float32


def test_create_query_embedding_returns_one_vector(
    monkeypatch,
):
    monkeypatch.setattr(
        embedding_service,
        "get_embedding_model",
        lambda: FakeEmbeddingModel(),
    )

    embedding = embedding_service.create_query_embedding(
        "What skills are required?"
    )

    assert isinstance(embedding, np.ndarray)
    assert embedding.shape == (2,)
    assert embedding.dtype == np.float32


def test_create_embeddings_returns_empty_array_for_empty_input():
    embeddings = embedding_service.create_embeddings([])

    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape == (0, 0)