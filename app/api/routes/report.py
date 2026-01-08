from fastapi import APIRouter, HTTPException, Query, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pathlib import Path
import uuid

from app.services.context_builder import build_context
from app.services.report_agent import generate_report
from app.services.pdf_generator import generate_report_pdf
from app.utils.json_cleanser import clean_llm_json
from app.db.session import SessionLocal
from app.db.models import UploadedFile

router = APIRouter(prefix="/report", tags=["Report"])


# ------------------ DB Dependency ------------------ #
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------ Shared Report Logic ------------------ #
def _generate_clean_report(file_ids: list[int], db: Session) -> dict:
    files = db.query(UploadedFile).filter(UploadedFile.id.in_(file_ids)).all()
    if not files:
        raise HTTPException(status_code=404, detail="Files not found")

    image_files = [f.file_path for f in files if f.file_type.startswith("image/")]
    csv_files = [f.file_path for f in files if f.file_type == "text/csv"]

    if not image_files and not csv_files:
        raise HTTPException(
            status_code=400,
            detail="No supported files found (CSV or image required)"
        )

    context = build_context(image_files, csv_files)
    raw_report = generate_report(context)

    try:
        return clean_llm_json(raw_report)
    except ValueError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Invalid JSON returned by report generator: {str(e)}"
        )


# ------------------ JSON API ------------------ #
@router.get(
    "/",
    summary="Generate analytical report as JSON",
    description=(
        "Generates a structured analytical report in JSON format using previously "
        "uploaded CSV and/or image files. The response includes key metrics, "
        "identified trends and correlations, actionable recommendations, and an "
        "executive summary. This endpoint is intended for programmatic consumption "
        "or further processing."
    ),
)
def generate_report_api(
    file_ids: list[int] = Query(..., description="List of uploaded file IDs to include in the report"),
    db: Session = Depends(get_db),
):
    clean_report = _generate_clean_report(file_ids, db)
    return {"report": clean_report}


# ------------------ PDF API ------------------ #
@router.get("/pdf",
              summary="Generate analytical report as PDF",
    description=(
        "Generates a professionally formatted PDF report based on the uploaded CSV "
        "and/or image files. The PDF includes an executive summary, key metrics, "
        "identified trends and correlations, and actionable recommendations. "
        "The generated file is returned as a downloadable PDF."
    ))
def generate_report_pdf_api(
    file_ids: list[int] = Query(...),
    db: Session = Depends(get_db),
):
    clean_report = _generate_clean_report(file_ids, db)

    pdf_dir = Path("app/storage/reports")
    pdf_dir.mkdir(parents=True, exist_ok=True)

    pdf_path = pdf_dir / f"report_{uuid.uuid4().hex}.pdf"

    # ✅ FIX HERE
    generate_report_pdf(clean_report, str(pdf_path))

    return FileResponse(
        path=pdf_path,
        media_type="application/pdf",
        filename="report.pdf",
    )
