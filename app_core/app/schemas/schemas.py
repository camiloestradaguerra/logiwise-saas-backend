from pydantic import BaseModel
from typing import Optional, List

# Esquema para cotizaciones
class QuoteCreate(BaseModel):
    shipment_id: int
    precio: float
    moneda: str
    tenant_id: Optional[str] = None

# Esquema para entidades (clientes/proveedores)
class EntityCreate(BaseModel):
    nombre: str
    tipo: str
    datos_fiscales: Optional[str] = None
    contacto: Optional[str] = None
    tenant_id: Optional[str] = None

# Esquema para documentos
class DocumentCreate(BaseModel):
    shipment_id: int
    tipo: str
    url: str
    tenant_id: Optional[str] = None

# Shipment
class ShipmentBase(BaseModel):
    origen: str
    destino: str
    tipo_carga: str
    estado: str
    moneda: str
    peso: float
    volumen: float
    tenant_id: Optional[str]

class ShipmentCreate(ShipmentBase):
    pass

class Shipment(ShipmentBase):
    id: int
    class Config:
        orm_mode = True

class ShipmentUpdate(BaseModel):
    origen: Optional[str] = None
    destino: Optional[str] = None
    tipo_carga: Optional[str] = None
    estado: Optional[str] = None
    moneda: Optional[str] = None
    peso: Optional[float] = None
    volumen: Optional[float] = None
    tenant_id: Optional[str] = None

# Quote
class QuoteCreate(BaseModel):
    shipment_id: int
    precio: float
    moneda: str
    tenant_id: Optional[str] = None

# Entity
class EntityCreate(BaseModel):
    nombre: str
    tipo: str
    datos_fiscales: Optional[str] = None
    contacto: Optional[str] = None
    tenant_id: Optional[str] = None

# Document
class DocumentCreate(BaseModel):
    shipment_id: int
    tipo: str
    url: str
    tenant_id: Optional[str] = None
