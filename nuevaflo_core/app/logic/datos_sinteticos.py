import random
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from ..models import models

# Listas de ejemplo para datos sintéticos
TENANTS = ["tenant1", "tenant2"]
CITIES = ["Bogotá", "Santiago", "Buenos Aires", "Lima", "Ciudad de México"]
CARGOS = ["FCL", "LCL", "Aéreo", "Terrestre"]
MODOS = [models.ShipmentMode.AEREO, models.ShipmentMode.MARITIMO, models.ShipmentMode.TERRESTRE]
MONEDAS = ["USD", "CLP", "COP", "ARS", "MXN"]
ESTADOS = [models.ShipmentState.DRAFT, models.ShipmentState.QUOTED, models.ShipmentState.BOOKED, models.ShipmentState.IN_TRANSIT, models.ShipmentState.DELIVERED]


def crear_datos_sinteticos(db: Session, n=10, tenants=None):
    if tenants is None:
        tenants = TENANTS
    for tenant_id in tenants:
        # Crear entidades
        for i in range(2):
            entity = models.Entity(
                tenant_id=tenant_id,
                name=f"Cliente {i+1} {tenant_id}",
                entity_type="cliente",
                tax_id=f"TAX-{random.randint(1000,9999)}",
                contact_name=f"Contacto {i+1}",
                contact_email=f"cliente{i+1}@{tenant_id}.com",
                contact_phone=f"+57{random.randint(10000000,99999999)}"
            )
            db.add(entity)
            db.commit()
            db.refresh(entity)
            # Crear Shipments
            for j in range(n):
                shipment = models.Shipment(
                    tenant_id=tenant_id,
                    mode=random.choice(MODOS),
                    origin=random.choice(CITIES),
                    destination=random.choice(CITIES),
                    cargo_type=random.choice(CARGOS),
                    state=random.choice(ESTADOS),
                    currency=random.choice(MONEDAS),
                    weight_kg=round(random.uniform(100, 2000), 2),
                    volume_cbm=round(random.uniform(1, 50), 2),
                    client_id=entity.id
                )
                db.add(shipment)
                db.commit()
                db.refresh(shipment)
                # Crear Quote
                quote = models.Quote(
                    tenant_id=tenant_id,
                    shipment_id=shipment.id,
                    buy_rate=round(random.uniform(1000, 5000), 2),
                    sell_rate=round(random.uniform(6000, 10000), 2),
                    currency=shipment.currency,
                    taxes=round(random.uniform(100, 500), 2),
                    created_at=datetime.utcnow() - timedelta(days=random.randint(0, 365))
                )
                db.add(quote)
                db.commit()
                # Crear Document
                doc = models.Document(
                    tenant_id=tenant_id,
                    shipment_id=shipment.id,
                    doc_type=random.choice(["BL", "AWB", "Factura"]),
                    file_path=f"/docs/{tenant_id}/doc_{shipment.id}.pdf",
                    uploaded_at=datetime.utcnow() - timedelta(days=random.randint(0, 365))
                )
                db.add(doc)
                db.commit()

# Ejemplo de uso:
# from app.logic.datos_sinteticos import crear_datos_sinteticos
# crear_datos_sinteticos(db, n=5)
