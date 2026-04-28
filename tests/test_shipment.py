"""
Archivo legacy: los tests de envíos han sido migrados a test_api_shipments.py y test_api_tenant.py.
Este archivo se mantiene solo como referencia histórica.
"""

from app.models.models import Shipment

def test_shipment_count(db_session):
    shipments = db_session.query(Shipment).all()
    assert len(shipments) > 0
    # Opcional: verifica que todos los shipments tengan tenant_id asignado
    assert all(s.tenant_id for s in shipments)
