from fastapi import APIRouter, UploadFile, File
from app.services.ingestion_service import ingest_file

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/",
    summary="Upload and ingest CSV or image files",
    description=(
        "Uploads one or more CSV or image files for analysis. "
        "Each file is stored locally, embedded for semantic search, "
        "and registered in the database. The uploaded files can later "
        "be used to generate analytical reports in JSON or PDF format."
    ),
    )
def upload_files(
    files: list[UploadFile] = File(
        ...,
        description="List of CSV or image files to be ingested"
    )
):
    results = []
    for file in files:
        results.append(ingest_file(file))
    return {"status": "success", "files": results}
