from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.pdf_service import extract_text_from_pdf
from app.services.text_service import split_text_into_chunks


router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = UPLOAD_DIR / file.filename

    file_content = await file.read()

    with open(file_path, "wb") as saved_file:
        saved_file.write(file_content)

    text = extract_text_from_pdf(str(file_path))
    chunks = split_text_into_chunks(text)

    return {
    "message": "PDF uploaded, extracted, and chunked successfully",
    "filename": file.filename,
    "text_length": len(text),
    "chunk_count": len(chunks),
    "text_preview": text[:500],
    "first_chunk_preview": chunks[0][:500] if chunks else ""
}