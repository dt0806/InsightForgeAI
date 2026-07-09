from app.services.pdf_service import extract_text_from_pdf
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException

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

    return {
    "message": "PDF uploaded successfully",
    "filename": file.filename,
    "pages_text_length": len(text),
    "preview": text[:500]
}