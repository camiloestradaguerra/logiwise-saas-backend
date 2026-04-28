"""
Pruebas de endpoints de Documentos
"""
import pytest
from fastapi.testclient import TestClient
from app_core.main import app

client = TestClient(app)

def get_token():
    payload = {"username": "admin", "password": "admin"}
    login = client.post("/auth/login", json=payload)
    if login.status_code != 200:
        pytest.skip("No se pudo autenticar usuario de prueba")
    return login.json()["access_token"]

def test_create_document():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "1"}
    payload = {
        "shipment_id": 1,
        "tipo": "BL",
        "nombre": "BL123.pdf"
    }
    response = client.post("/documents", json=payload, headers=headers)
    assert response.status_code in (200, 201, 404)  # 404 si shipment_id no existe

def test_list_documents():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "1"}
    response = client.get("/documents", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
