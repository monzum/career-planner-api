from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import applications

app = FastAPI(title=settings.app_name)

app.include_router(
    applications.router,
    prefix="/applications",
    tags=["applications"]
)

@app.get("/health")
def health():
    return {"status": "ok"}
