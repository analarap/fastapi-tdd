from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_existing_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Item 1"}

def test_get_nonexistent_item():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item não existe"}
