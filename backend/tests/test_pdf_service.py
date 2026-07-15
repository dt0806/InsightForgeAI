from pathlib import Path

import fitz

from app.services.pdf_service import extract_text_from_pdf


def test_extract_text_from_pdf_returns_text(tmp_path):
    pdf_path = tmp_path / "sample.pdf"

    document = fitz.open()
    page = document.new_page()
    page.insert_text(
        (72, 72),
        "InsightForgeAI extracts text from PDF files."
    )
    document.save(pdf_path)
    document.close()

    extracted_text = extract_text_from_pdf(
        str(pdf_path)
    )

    assert "InsightForgeAI extracts text" in extracted_text


def test_extract_text_from_empty_pdf_returns_empty_string(
    tmp_path,
):
    pdf_path = tmp_path / "empty.pdf"

    document = fitz.open()
    document.new_page()
    document.save(pdf_path)
    document.close()

    extracted_text = extract_text_from_pdf(
        str(pdf_path)
    )

    assert extracted_text.strip() == ""