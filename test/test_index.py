from fastapi.testclient import TestClient
from app.index import app  
client = TestClient(app)

def test_create_item():
    item_data = {
        "id": 1,
        "name": "Example Item",
        "description": "Example Description",
        "price": 29.99,
        "tax": 2.50
    }

    response = client.post("/items/", json=item_data)

    assert response.status_code == 200
    assert response.json() == item_data

def test_search_item_found():
    item_data = {
        "id": 2,
        "name": "Found Item",
        "description": "Found Description",
        "price": 39.99,
        "tax": 3.50
    }
    item_id = item_data["id"]

    # Create the item first
    client.post("/items/", json=item_data)

    response = client.get(f"/items/{item_id}")

    assert response.status_code == 200
    assert response.json()["result"] == [item_data]

def test_search_item_not_found():
    item_id = 999  # Assuming this ID is not present in the item_list

    response = client.get(f"/items/{item_id}")

    assert response.status_code == 200
    assert response.json()["result"] == ["Not found"]
