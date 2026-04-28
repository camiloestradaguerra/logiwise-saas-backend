"""
Multi-tenant/SaaS support for FastAPI app.
This module provides a basic tenant identification and data separation strategy.
"""
from fastapi import Request, HTTPException, Depends
from typing import Callable

# Simulación de tenants registrados
TENANTS = {
    "tenant1": {"name": "Cliente A"},
    "tenant2": {"name": "Cliente B"},
}

def get_tenant_from_header(request: Request):
    tenant_id = request.headers.get("X-Tenant-ID")
    if not tenant_id or tenant_id not in TENANTS:
        raise HTTPException(status_code=400, detail="Tenant inválido o no especificado")
    return tenant_id

# Dependencia para inyectar tenant en endpoints
async def tenant_dependency(tenant_id: str = Depends(get_tenant_from_header)):
    return tenant_id

# Ejemplo de uso en endpoint:
# @router.get("/shipments/")
# async def list_shipments(tenant_id: str = Depends(tenant_dependency)):
#     # Filtrar datos por tenant_id
#     ...

# NOTA: Para una implementación real, deberías asociar cada registro de la base de datos a un tenant_id
# y filtrar todas las consultas por ese campo. También puedes usar middlewares para inyectar el tenant globalmente.
