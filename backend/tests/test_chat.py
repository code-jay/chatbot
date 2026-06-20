from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_requires_auth():
    response = client.post(
        "/chat/stream",
        json={
            "message": "Hello"
        }
    )

    assert response.status_code == 401