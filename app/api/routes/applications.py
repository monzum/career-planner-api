# app/api/routes/applications.py

"""
Application Routes (API Layer)

This module defines all HTTP endpoints related to job applications.

Responsibilities:
- Handle HTTP requests and responses
- Validate inputs (via schemas)
- Call service layer for business logic
- Return appropriate HTTP responses

NOTE:
All core logic is delegated to the service layer (job_service).
"""

from fastapi import APIRouter, HTTPException
from typing import List

from app.schemas.application import (
    JobApplication,
    JobApplicationCreate,
    JobApplicationUpdate
)

from app.services import job_service

# Create router instance for application-related endpoints
router = APIRouter()


# ------------------------------------------------------------------
# Create a New Job Application
# ------------------------------------------------------------------
@router.post("/", response_model=JobApplication)
async def create_application(data: JobApplicationCreate):
    """
    Creates a new job application.

    Args:
        data (JobApplicationCreate): Incoming request payload

    Returns:
        JobApplication: Newly created application
    """
    return job_service.create_application(data)


# ------------------------------------------------------------------
# Get All Job Applications
# ------------------------------------------------------------------
@router.get("/", response_model=List[JobApplication])
async def list_applications():
    """
    Retrieves all job applications.

    Returns:
        List[JobApplication]: List of all stored applications
    """
    return job_service.list_applications()


# ------------------------------------------------------------------
# Get a Single Job Application by ID
# ------------------------------------------------------------------
@router.get("/{app_id}", response_model=JobApplication)
async def get_application(app_id: int):
    """
    Retrieves a specific job application by ID.

    Args:
        app_id (int): Unique identifier of the application

    Returns:
        JobApplication: Matching application

    Raises:
        HTTPException: 404 if application not found
    """
    app = job_service.get_application(app_id)

    if not app:
        raise HTTPException(status_code=404, detail="Application not found")

    return app


# ------------------------------------------------------------------
# Update an Existing Job Application
# ------------------------------------------------------------------
@router.patch("/{app_id}", response_model=JobApplication)
async def update_application(app_id: int, updates: JobApplicationUpdate):
    """
    Updates fields of an existing job application.

    Args:
        app_id (int): Application ID
        updates (JobApplicationUpdate): Fields to update

    Returns:
        JobApplication: Updated application

    Raises:
        HTTPException: 404 if application not found
    """
    app = job_service.update_application(app_id, updates)

    if not app:
        raise HTTPException(status_code=404, detail="Application not found")

    return app


# ------------------------------------------------------------------
# Delete a Job Application
# ------------------------------------------------------------------
@router.delete("/{app_id}")
async def delete_application(app_id: int):
    """
    Deletes a job application by ID.

    Args:
        app_id (int): Application ID

    Returns:
        dict: Confirmation message

    Raises:
        HTTPException: 404 if application not found
    """
    success = job_service.delete_application(app_id)

    if not success:
        raise HTTPException(status_code=404, detail="Application not found")

    return {"message": "Deleted successfully"}