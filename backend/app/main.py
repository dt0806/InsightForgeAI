from app.api.upload import router as upload_router
from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="Atlas AI API",
    description="Backend API for Atlas AI - Enterprise Knowledge and Data Intelligence Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Atlas AI API",
        "status": "running"
    }


app.include_router(health_router)
app.include_router(upload_router)