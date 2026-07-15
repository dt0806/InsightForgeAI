from app.services.text_service import split_text_into_chunks


def test_split_text_into_chunks_creates_multiple_chunks():
    text = "A" * 2500

    chunks = split_text_into_chunks(text)

    assert len(chunks) > 1
    assert all(isinstance(chunk, str) for chunk in chunks)
    assert all(len(chunk) > 0 for chunk in chunks)


def test_split_text_into_chunks_returns_empty_list_for_empty_text():
    chunks = split_text_into_chunks("")

    assert chunks == []