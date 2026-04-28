"""
Pruebas de multi-tenant y aislamiento de datos
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

def test_tenant_isolation():
    token = get_token()
    # Crear shipment con tenant 1
    headers1 = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "1"}
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
    r1 = client.post("/shipments", json=payload, headers=headers1)
    # Listar con tenant 2 (no debería ver el shipment anterior)
    headers2 = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "2"}
    r2 = client.get("/shipments", headers=headers2)
    assert all(s["origen"] != "BOG" for s in r2.json())
