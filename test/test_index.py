from fastapi.testclient import TestClient
from app.index import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI"}

def test_create_item():
    item_data = {
        "id": 1,
        "name": "Test Item",
        "description": "Test Description",
        "price": 19.99,
        "tax": 2.0
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data

def test_read_item_found():
    item_id = 1
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"result": {"id": 1, "name": "Test Item", "description": "Test Description", "price": 19.99, "tax": 2.0}}

def test_read_item_not_found():
    item_id = 2
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"result": "Not found"}

