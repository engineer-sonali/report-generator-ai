from fastapi import APIRouter, HTTPException, Query
from app.services.context_builder import build_context
from app.services.report_agent import generate_report
from app.db.session import SessionLocal
from app.db.models import UploadedFile

router = APIRouter(prefix="/report", tags=["Report"])

@router.get("/")
def generate_report_api(file_ids: list[int] = Query(..., description="List of uploaded file IDs to generate report")):
    db = SessionLocal()

    # Fetch files from DB
    files = db.query(UploadedFile).filter(UploadedFile.id.in_(file_ids)).all()
    if not files:
        raise HTTPException(status_code=404, detail="Files not found")

    # Collect paths
    image_files = [f.file_path for f in files if f.file_type.startswith("image/")]
    csv_files = [f.file_path for f in files if f.file_type == "text/csv"]

    # Build context and generate report
    context = build_context(image_files, csv_files)
    report = generate_report(context)

    return {"report": report}
