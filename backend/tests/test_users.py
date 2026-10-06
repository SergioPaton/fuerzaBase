import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_create_user_success():
    payload = {
        "first_name": "Ana",
        "last_name": "Gomez",
        "email": "ana.gomez@test.com",
        "password": "Abc123456",
        "role": "client"
    }
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert data["email"] == "ana.gomez@test.com"
    assert data["role"] == "client"

def test_create_user_weak_password():
    payload = {
        "first_name": "Luis",
        "last_name": "Perez",
        "email": "luis@test.com",
        "password": "123",
        "role": "client"
    }
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 422

def test_create_user_invalid_role():
    payload = {
        "first_name": "Maria",
        "last_name": "Lopez",
        "email": "maria@test.com",
        "password": "Abc123456",
        "role": "admin"
    }
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 422

def test_create_user_invalid_email():
    payload = {
        "first_name": "Carlos",
        "last_name": "Ruiz",
        "email": "no-es-email",
        "password": "Abc123456",
        "role": "independent"
    }
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 422

def test_create_user_duplicate_email():
    payload = {
        "first_name": "Pedro",
        "last_name": "Sanz",
        "email": "pedro@test.com",
        "password": "Abc123456",
        "role": "trainer"
    }
    client.post("/api/v1/users/", json=payload)
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 400
