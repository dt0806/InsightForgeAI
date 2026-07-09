from fastapi import FastAPI

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


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "Atlas AI",
        "version": "1.0.0"
    }