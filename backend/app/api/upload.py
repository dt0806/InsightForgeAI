from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/upload/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    return {
        "message": "PDF received successfully",
        "filename": file.filename,
        "content_type": file.content_type
    }