from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, world!"}

def test_status():
    r = client.get("/status")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_user():
    r = client.get("/users/7")
    assert r.status_code == 200
    body = r.json()
    assert body["user_id"] == 7
    assert "name" in body
