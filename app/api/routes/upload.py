from fastapi import APIRouter, UploadFile, File
from app.services.ingestion_service import ingest_file

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
def upload_files(files: list[UploadFile] = File(...)):
    results = []
    for file in files:
        results.append(ingest_file(file))
    return {"status": "success", "files": results}
