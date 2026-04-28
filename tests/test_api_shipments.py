"""
Pruebas CRUD y lógica de envíos (Shipments)
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

def test_create_shipment():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "1"}
    payload = {
        "modo": "aéreo",
        "origen": "BOG",
        "destino": "MIA",
        "tipo_carga": "general",
        "estado": "Draft",
        "moneda": "USD",
        "peso": 1000,
        "volumen": 2.5
    }
    response = client.post("/shipments", json=payload, headers=headers)
    assert response.status_code in (200, 201)
    data = response.json()
    assert data["origen"] == "BOG"

def test_list_shipments():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "1"}
    response = client.get("/shipments", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_shipment():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "1"}
    # Crear primero
    payload = {
        "modo": "marítimo",
        "origen": "LIM",
        "destino": "MIA",
        "tipo_carga": "reefer",
        "estado": "Draft",
        "moneda": "USD",
        "peso": 500,
        "volumen": 1.2
    }
    create = client.post("/shipments", json=payload, headers=headers)
    shipment_id = create.json()["id"]
    # Actualizar
    update = {"estado": "Quoted"}
    response = client.patch(f"/shipments/{shipment_id}", json=update, headers=headers)
    assert response.status_code in (200, 204)

def test_delete_shipment():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "1"}
    # Crear primero
    payload = {
        "modo": "terrestre",
        "origen": "SCL",
        "destino": "EZE",
        "tipo_carga": "peligrosa",
        "estado": "Draft",
        "moneda": "CLP",
        "peso": 200,
        "volumen": 0.8
    }
    create = client.post("/shipments", json=payload, headers=headers)
    shipment_id = create.json()["id"]
    # Eliminar
    response = client.delete(f"/shipments/{shipment_id}", headers=headers)
    assert response.status_code in (200, 204, 202)
