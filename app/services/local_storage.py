import shutil
from pathlib import Path

UPLOAD_DIR = Path("app/storage/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def upload_file(file, filename: str) -> str:
    file_path = UPLOAD_DIR / filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file, buffer)
    return str(file_path)
