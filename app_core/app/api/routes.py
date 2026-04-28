
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app_core.app.models import models
from app_core.app.schemas import schemas
from app_core.app.logic import cotizacion


from app_core.app.api.tenant import tenant_dependency
from app_core.app.database import get_db
from app_core.app.api.auth import get_current_user

router = APIRouter()

    # get_db ahora importado desde database.py

# CRUD Shipments
@router.post("/shipments/")
def create_shipment(
    shipment: schemas.ShipmentCreate,
    db: Session = Depends(get_db),
    tenant_id: str = Depends(tenant_dependency),
    current_user=Depends(get_current_user)
):
    # Mapear campos del esquema español a los del modelo
    data = shipment.dict()
    mapped = {
        "mode": models.ShipmentMode.AEREO,  # Valor fijo de ejemplo, puedes ajustar según lógica
        "origin": data["origen"],
        "destination": data["destino"],
        "cargo_type": data["tipo_carga"],
        "state": models.ShipmentState.DRAFT,  # Valor fijo de ejemplo, puedes ajustar según lógica
        "currency": data["moneda"],
        "weight_kg": data["peso"],
        "volume_cbm": data["volumen"],
        "tenant_id": tenant_id
        # "client_id": ... # Si tienes lógica para asociar cliente
    }
    db_shipment = models.Shipment(**mapped)
    db.add(db_shipment)
    db.commit()
    db.refresh(db_shipment)
    return db_shipment

@router.get("/shipments/")
def list_shipments(
    db: Session = Depends(get_db),
    tenant_id: str = Depends(tenant_dependency),
    current_user=Depends(get_current_user)
):
    # Devuelve solo los envíos del tenant actual
    return db.query(models.Shipment).filter(models.Shipment.tenant_id == tenant_id).all()

@router.get("/shipments/{shipment_id}")
def get_shipment(
    shipment_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # Implementar obtención de shipment
    pass

@router.put("/shipments/{shipment_id}")
def update_shipment(
    shipment_id: int,
    shipment: schemas.ShipmentUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # Implementar actualización de shipment
    pass

@router.delete("/shipments/{shipment_id}")
def delete_shipment(
    shipment_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # Implementar borrado de shipment
    pass

# CRUD Quotes
@router.post("/quotes/")
def create_quote(quote: schemas.QuoteCreate, db: Session = Depends(get_db)):
    # Implementar creación de quote
    pass

# CRUD Entities
@router.post("/entities/")
def create_entity(entity: schemas.EntityCreate, db: Session = Depends(get_db)):
    # Implementar creación de entity
    pass

# CRUD Documents
@router.post("/documents/")
def create_document(document: schemas.DocumentCreate, db: Session = Depends(get_db)):
    # Implementar creación de documento
    pass

# Endpoint para cambiar estado de un envío
@router.post("/shipments/{shipment_id}/change_state/")
def change_shipment_state(shipment_id: int, new_state: str, db: Session = Depends(get_db)):
    # Implementar cambio de estado
    pass
