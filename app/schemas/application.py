from pydantic import BaseModel
from typing import Optional

class JobApplicationCreate(BaseModel):
    company: str
    role: str
    location: str
    status: str = "applied"
    notes: Optional[str] = None

class JobApplication(JobApplicationCreate):
    id: int
