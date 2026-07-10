from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.chunk_service import create_chunk_records
from app.services.pdf_service import extract_text_from_pdf
from app.services.storage_service import save_chunk_records
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

    document_id = str(uuid4())

    chunk_records = create_chunk_records(
        chunks=chunks,
        document_id=document_id,
        source_file=file.filename
    )

    processed_file_path = save_chunk_records(
        document_id=document_id,
        records=chunk_records
    )

    return {
        "message": "PDF uploaded and processed successfully",
        "document_id": document_id,
        "filename": file.filename,
        "text_length": len(text),
        "chunk_count": len(chunk_records),
        "processed_file": str(processed_file_path),
        "first_chunk": chunk_records[0] if chunk_records else None
    }