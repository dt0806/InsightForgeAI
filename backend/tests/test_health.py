from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint_returns_healthy_status():
    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "healthy",
        "application": "InsightForgeAI",
        "version": "1.0.0",
    }


def test_root_endpoint_returns_welcome_message():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Welcome to InsightForgeAI API",
        "status": "running",
    }