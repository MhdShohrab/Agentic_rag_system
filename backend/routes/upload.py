# backend/routes/upload.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import Annotated
import os

# Import your RAG function
from rag.rag_pipeline import build_vector_db_multiple

router = APIRouter()

# Constants
MIN_FILES = 1
MAX_FILES = 3
UPLOAD_DIR = "data"

# Ensure upload folder exists
os.makedirs(UPLOAD_DIR, exist_ok=True)          #manually i can set path but i used os here.

@router.post("/upload")
async def upload_pdfs(files: Annotated[list[UploadFile], File(...)]):       #Annotated this is important.
    """
    Upload 1-3 PDFs and create vector DB
    """

    # Step 1: Validate file count
    if len(files) < MIN_FILES:
        raise HTTPException(
            status_code=400,
            detail="At least 1 PDF is required"
        )

    if len(files) > MAX_FILES:
        raise HTTPException(
            status_code=400,
            detail="Maximum 3 PDFs allowed"
        )

    file_paths = []

    # Step 2: Save files
    for file in files:

        # Validate file type
        if not file.filename.endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail=f"{file.filename} is not a PDF"
            )

        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        file_paths.append(file_path)        #in this line all files are appended.

    # Step 3: Call RAG pipeline
    try:
        build_vector_db_multiple(file_paths)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing PDFs: {str(e)}"
        )

    # Step 4: Return success response
    return {
        "message": f"{len(files)} PDF(s) uploaded successfully",
        "files": [file.filename for file in files]
    }