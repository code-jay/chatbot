from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_upload_requires_auth():
    with open("sample.txt", "w") as f:
        f.write("Hello World")

    with open("sample.txt", "rb") as file:
        response = client.post(
            "/files/upload",
            files={"file": ("sample.txt", file, "text/plain")}
        )

    assert response.status_code == 401