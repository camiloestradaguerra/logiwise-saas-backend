"""
Pruebas de autenticación y autorización (login, roles, acceso protegido)
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_success():
    payload = {"username": "admin", "password": "admin"}
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_fail():
    payload = {"username": "admin", "password": "wrongpass"}
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 401

def test_access_protected_without_token():
    response = client.get("/shipments")
    assert response.status_code in (401, 403)

def test_access_protected_with_invalid_token():
    headers = {"Authorization": "Bearer invalidtoken", "X-Tenant-ID": "1"}
    response = client.get("/shipments", headers=headers)
    assert response.status_code in (401, 403)

# Puedes agregar más pruebas de roles si tienes endpoints diferenciados
