from fastapi import APIRouter
from pydantic import BaseModel, Field


router = APIRouter(
    tags=["Health"],
)


class HealthResponse(BaseModel):
    status: str = Field(
        ...,
        description="Current application health status",
        examples=["healthy"],
    )

    application: str = Field(
        ...,
        description="Application name",
        examples=["InsightForgeAI"],
    )

    version: str = Field(
        ...,
        description="Current API version",
        examples=["1.0.0"],
    )


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Check API health",
    description="Returns the current status, application name, and API version.",
)
def health_check():
    return {
        "status": "healthy",
        "application": "InsightForgeAI",
        "version": "1.0.0",
    }