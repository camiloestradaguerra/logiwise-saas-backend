"""
Pruebas de errores y edge cases
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

def test_create_shipment_missing_fields():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "1"}
    payload = {"origen": "BOG"}  # Falta info obligatoria
    response = client.post("/shipments", json=payload, headers=headers)
    assert response.status_code in (400, 422)

def test_create_duplicate_entity():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "1"}
    payload = {
        "nombre": "Cliente Duplicado",
        "tipo": "cliente",
        "rfc": "RFC999999",
        "pais": "CO",
        "email": "dup@demo.com"
    }
    client.post("/entities", json=payload, headers=headers)
    response = client.post("/entities", json=payload, headers=headers)
    assert response.status_code in (400, 409, 422)
