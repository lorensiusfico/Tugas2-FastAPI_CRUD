from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users", json={
        "username": "john123",
        "email": "john@example.com",
        "password": "Password1!",
        "role": "admin"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "john123"
    assert data["email"] == "john@example.com"

def test_get_all_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert "username" in response.json()

def test_update_user():
    response = client.put("/users/1", json={
        "username": "updatedname"
    })
    assert response.status_code == 200
    assert response.json()["username"] == "updatedname"

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 204