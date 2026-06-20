from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_conversations():
    response = client.get("/conversations")

    assert response.status_code in [200, 401]