"""
Job Service Layer

This module contains all business logic related to job applications.

It acts as an abstraction layer between:
- API routes (controllers)
- Data storage (currently in-memory, later PostgreSQL)

Benefits:
- Keeps routes clean and focused on request/response handling
- Makes it easy to swap the database later without changing routes
- Aligns with microservice-ready architecture
"""

from typing import List
from app.schemas.application import (
    JobApplication,
    JobApplicationCreate,
    JobApplicationUpdate
)

# ------------------------------------------------------------------
# Temporary In-Memory Storage
# ------------------------------------------------------------------
# This simulates a database for now.
# Will be replaced with PostgreSQL (RDS) in the next phase.

_db = []            # List to store job applications
_id_counter = 1     # Simple auto-incrementing ID


# ------------------------------------------------------------------
# Create a New Job Application
# ------------------------------------------------------------------
def create_application(data: JobApplicationCreate) -> JobApplication:
    """
    Creates a new job application and stores it in memory.

    Args:
        data (JobApplicationCreate): Incoming request data

    Returns:
        JobApplication: Newly created application with ID
    """
    global _id_counter

    # Create a new JobApplication object with unique ID
    new_app = JobApplication(
        id=_id_counter,
        **data.dict()
    )

    # Store in "database"
    _db.append(new_app)

    # Increment ID for next record
    _id_counter += 1

    return new_app


# ------------------------------------------------------------------
# Retrieve All Applications
# ------------------------------------------------------------------
def list_applications() -> List[JobApplication]:
    """
    Returns all stored job applications.

    Returns:
        List[JobApplication]: List of applications
    """
    return _db


# ------------------------------------------------------------------
# Retrieve a Single Application by ID
# ------------------------------------------------------------------
def get_application(app_id: int) -> JobApplication:
    """
    Fetches a job application by its ID.

    Args:
        app_id (int): Application ID

    Returns:
        JobApplication | None: Matching application or None if not found
    """
    for app in _db:
        if app.id == app_id:
            return app
    return None


# ------------------------------------------------------------------
# Update an Existing Application
# ------------------------------------------------------------------
def update_application(app_id: int, updates: JobApplicationUpdate) -> JobApplication:
    """
    Updates fields of an existing job application.

    Only fields provided in the request will be updated.

    Args:
        app_id (int): Application ID
        updates (JobApplicationUpdate): Fields to update

    Returns:
        JobApplication | None: Updated application or None if not found
    """
    for app in _db:
        if app.id == app_id:

            # Extract only fields that were provided (partial update)
            data = updates.dict(exclude_unset=True)

            # Dynamically update attributes
            for key, value in data.items():
                setattr(app, key, value)

            return app

    return None


# ------------------------------------------------------------------
# Delete an Application
# ------------------------------------------------------------------
def delete_application(app_id: int) -> bool:
    """
    Deletes a job application by ID.

    Args:
        app_id (int): Application ID

    Returns:
        bool: True if deleted, False if not found
    """
    global _db

    for app in _db:
        if app.id == app_id:
            # Remove the application from the list
            _db = [a for a in _db if a.id != app_id]
            return True

    return False