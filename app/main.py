# app/main.py
from fastapi import FastAPI
from app.api.routes import upload, report

app = FastAPI(
    title="AI Report Generator",
    description="Generate business analytics reports from CSVs and images",
    version="1.0"
)

app.include_router(upload.router)
app.include_router(report.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)