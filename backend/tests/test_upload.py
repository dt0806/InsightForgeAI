from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_upload_rejects_non_pdf_file():
    fake_text_file = BytesIO(b"This is not a PDF file.")

    response = client.post(
        "/upload/pdf",
        files={
            "file": (
                "notes.txt",
                fake_text_file,
                "text/plain",
            )
        },
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Only PDF files are allowed."
    }