from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.application import JobApplication, JobApplicationCreate

router = APIRouter()

_db = []
_id_counter = 1


@router.post("/", response_model=JobApplication)
def create_application(app: JobApplicationCreate):
    global _id_counter
    record = JobApplication(id=_id_counter, **app.dict())
    _db.append(record)
    _id_counter += 1
    return record


@router.get("/", response_model=List[JobApplication])
def list_applications():
    return _db


@router.get("/{app_id}", response_model=JobApplication)
def get_application(app_id: int):
    for app in _db:
        if app.id == app_id:
            return app
    raise HTTPException(status_code=404, detail="Application not found")


@router.delete("/{app_id}")
def delete_application(app_id: int):
    global _db
    _db = [a for a in _db if a.id != app_id]
    return {"deleted": app_id}
