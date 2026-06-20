from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register():
    response = client.post(
        "/auth/register",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "password": "password123",
            "role": "user"
        }
    )

    assert response.status_code in [200, 400]