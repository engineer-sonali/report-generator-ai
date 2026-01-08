# app/main.py
from fastapi import FastAPI
from app.api.routes import upload, report

app = FastAPI(
    title="Vision-Language Report Generator",
    description="Generate business analytics reports from CSVs and images",
    version="1.0"
)

app.include_router(upload.router, prefix="/upload")
app.include_router(report.router, prefix="/report")
