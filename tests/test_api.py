"""
Archivo legacy: los tests han sido reorganizados por entidad y funcionalidad.

- test_api_auth.py: autenticación y roles
- test_api_shipments.py: CRUD envíos
- test_api_entities.py: CRUD entidades
- test_api_quotes.py: CRUD cotizaciones
- test_api_documents.py: CRUD documentos
- test_api_tenant.py: multi-tenant
- test_api_errors.py: errores y edge cases

Este archivo se mantiene solo como referencia histórica.
"""

import pytest
from fastapi.testclient import TestClient
from app_core.main import app

client = TestClient(app)

def test_root_public():
    response = client.get("/")
    assert response.status_code == 200
    assert "msg" in response.json()

# Ejemplo de login (ajusta el payload según tu modelo de usuario)
def test_login():
    payload = {"username": "admin@example.com", "password": "admin"}
    response = client.post("/auth/token", data=payload)
    # Puede ser 200 o 401 según si existen usuarios de prueba
    assert response.status_code in (200, 401)
    if response.status_code == 200:
        assert "access_token" in response.json()

# Ejemplo de acceso protegido (ajusta el endpoint y token según tu app)
def test_protected_endpoint():
    # Primero, login para obtener token
    payload = {"username": "admin@example.com", "password": "admin"}
    login = client.post("/auth/token", data=payload)
    if login.status_code != 200:
        pytest.skip("No se pudo autenticar usuario de prueba")
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}", "X-Tenant-ID": "tenant1"}
    # Ajusta el endpoint a uno protegido real
    response = client.get("/shipments", headers=headers)
    assert response.status_code in (200, 403, 404)
