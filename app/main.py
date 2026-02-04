from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import applications
from app.core.middleware import logging_middleware

# Create the FastAPI application instance
app = FastAPI(title=settings.app_name)
app.middleware("http")(logging_middleware)


app.include_router(
    applications.router,
    prefix="/api/v1/applications",
    tags=["applications"]
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {
        "service": "career-planner-api",
        "version": "0.1.0",
        "status": "running"
    }
