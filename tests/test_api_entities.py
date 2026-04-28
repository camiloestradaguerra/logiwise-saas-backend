"""
Pruebas de endpoints de Entities (clientes/proveedores)
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_token():
    payload = {"username": "admin", "password": "admin"}
    login = client.post("/auth/login", json=payload)
    if login.status_code != 200:
        pytest.skip("No se pudo autenticar usuario de prueba")
    return login.json()["access_token"]

def test_create_entity():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "1"}
    payload = {
        "nombre": "Cliente Demo",
        "tipo": "cliente",
        "rfc": "RFC123456",
        "pais": "CO",
        "email": "cliente@demo.com"
    }
    response = client.post("/entities", json=payload, headers=headers)
    assert response.status_code in (200, 201)
    data = response.json()
    assert data["nombre"] == "Cliente Demo"

def test_list_entities():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "1"}
    response = client.get("/entities", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
