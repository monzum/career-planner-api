from pydantic import BaseModel
from typing import Optional
from typing import Literal

# Allowed lifecycle states for a tracked job application.
# Using Literal keeps validation strict so the API only accepts known values.
StatusType = Literal[
    "applied",
    "interview",
    "offer",
    "rejected",
    "accepted"
]

class JobApplicationCreate(BaseModel):
    # Schema for incoming POST requests when a user creates a new job application.
    # Pydantic validates these fields automatically before the request reaches
    # the service layer, which keeps route handlers simple and predictable.
    company: str
    role: str
    location: str
    status: StatusType = "applied"
    notes: Optional[str] = None

class JobApplication(JobApplicationCreate):
    # Full application model returned by the API.
    # This reuses the create schema and adds the server-generated ID field that
    # identifies each stored application record.
    id: int

class JobApplicationUpdate(BaseModel):
    # Schema for PATCH requests.
    # All fields are optional because clients may update only part of the
    # application instead of resending the complete object.
    status: Optional[StatusType] = None
    notes: Optional[str] = None
