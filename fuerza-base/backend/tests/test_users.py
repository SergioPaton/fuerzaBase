"""
Tests de integración — endpoint POST /api/v1/users/
Usa TestClient de FastAPI con base de datos SQLite en memoria.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.core.database import get_db
from app.infrastructure.db.models import Base

# Base de datos SQLite en memoria para tests — no afecta a la BD real
TEST_DATABASE_URL = "sqlite:///./test_fuerza_base.db"
test_engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(autouse=True)
def setup_db():
    """Crea las tablas antes de cada test y las elimina después."""
    Base.metadata.create_all(bind=test_engine)
    app.dependency_overrides[get_db] = override_get_db
    yield
    Base.metadata.drop_all(bind=test_engine)
    app.dependency_overrides.clear()


client = TestClient(app)


def test_create_user_success():
    payload = {
        "first_name": "Ana",
        "last_name": "Gomez",
        "email": "ana.gomez@test.com",
        "password": "Abc123456",
        "role": "client",
    }
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "ana.gomez@test.com"
    assert data["role"] == "client"
    assert "id" in data


def test_create_user_weak_password():
    payload = {
        "first_name": "Luis",
        "last_name": "Perez",
        "email": "luis@test.com",
        "password": "123",
        "role": "client",
    }
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 422


def test_create_user_invalid_role():
    payload = {
        "first_name": "Maria",
        "last_name": "Lopez",
        "email": "maria@test.com",
        "password": "Abc123456",
        "role": "admin",
    }
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 422


def test_create_user_invalid_email():
    payload = {
        "first_name": "Carlos",
        "last_name": "Ruiz",
        "email": "no-es-email",
        "password": "Abc123456",
        "role": "independent",
    }
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 422


def test_create_user_duplicate_email():
    payload = {
        "first_name": "Pedro",
        "last_name": "Sanz",
        "email": "pedro@test.com",
        "password": "Abc123456",
        "role": "trainer",
    }
    client.post("/api/v1/users/", json=payload)
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 400


def test_create_user_short_first_name():
    payload = {
        "first_name": "A",
        "last_name": "Lopez",
        "email": "a@test.com",
        "password": "Abc123456",
        "role": "client",
    }
    response = client.post("/api/v1/users/", json=payload)
    assert response.status_code == 422
