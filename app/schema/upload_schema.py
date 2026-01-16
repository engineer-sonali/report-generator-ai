from pydantic import BaseModel
from typing import List

class UploadedFileResponse(BaseModel):
    file_id: int
    filename: str
    vector_id: str

class UploadResponse(BaseModel):
    status: str
    files: List[UploadedFileResponse]
