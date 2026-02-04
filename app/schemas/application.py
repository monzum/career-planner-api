from pydantic import BaseModel
from typing import Optional
from typing import Literal

StatusType = Literal[
    "applied",
    "interview",
    "offer",
    "rejected",
    "accepted"
]

class JobApplicationCreate(BaseModel):
    company: str
    role: str
    location: str
    status: StatusType = "applied"
    notes: Optional[str] = None

class JobApplication(JobApplicationCreate):
    id: int

class JobApplicationUpdate(BaseModel):
    status: Optional[StatusType] = None
    notes: Optional[str] = None