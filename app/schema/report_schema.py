from pydantic import BaseModel
from typing import Dict, Any

class ReportResponse(BaseModel):
    report: Dict[str, Any]
