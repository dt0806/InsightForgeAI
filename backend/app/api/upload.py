from pathlib import Path
from uuid import uuid4
import traceback

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.chunk_service import create_chunk_records
from app.services.pdf_service import extract_text_from_pdf
from app.services.storage_service import save_chunk_records, save_embeddings
from app.services.text_service import split_text_into_chunks
from app.services.embedding_service import create_embeddings

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

    try:
        embeddings = create_embeddings(
            [record["content"] for record in chunk_records]
        )

        embedding_file_path = save_embeddings(
            document_id=document_id,
            embeddings=embeddings
        )

    except Exception as error:
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=f"Embedding processing failed: {type(error).__name__}: {error}"
        )
    
    return {
    "message": "PDF uploaded, processed, and embedded successfully",
    "document_id": document_id,
    "filename": file.filename,
    "text_length": len(text),
    "chunk_count": len(chunk_records),
    "embedding_count": len(embeddings),
    "embedding_dimensions": (
        int(embeddings.shape[1])
        if embeddings.ndim == 2 and len(embeddings) > 0
        else 0
    ),
    "processed_file": str(processed_file_path),
    "embedding_file": str(embedding_file_path),
    "first_chunk": chunk_records[0] if chunk_records else None
    }