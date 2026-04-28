
import pytest
from app_core.app.database import engine
from app_core.app.models.models import Base

@pytest.fixture(scope="session", autouse=True)
def create_test_tables():
    # Crear todas las tablas antes de cualquier test
    Base.metadata.create_all(bind=engine)
    yield
    # Limpiar (opcional):
    # Base.metadata.drop_all(bind=engine)

"""
Fixture de pytest para base de datos temporal y datos sintéticos

Este fixture inicializa una base de datos SQLite en memoria y la puebla con datos sintéticos
usando la lógica existente. Cada test recibe una base limpia y aislada.

Ejemplo de uso:

    def test_shipment_count(db_session):
        shipments = db_session.query(Shipment).all()
        assert len(shipments) > 0

Recomendaciones:
- Usa este fixture en todos los tests que requieran acceso a la base de datos.
- No mezcles datos entre tests: cada uno recibe su propia base en memoria.
- Puedes modificar la cantidad de datos sintéticos cambiando el parámetro n.
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app_core.app.models.models import Base
from app_core.app.logic.datos_sinteticos import crear_datos_sinteticos


@pytest.fixture(scope="function")
def db_session():
    """
    Inicializa una base de datos SQLite en memoria y la puebla con datos sintéticos.
    Cada test recibe una base limpia y aislada.
    """
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    crear_datos_sinteticos(db, n=5)  # Puedes ajustar n para más/menos datos
    yield db
    db.close()

# Ejemplo de uso en un test
# def test_shipment_count(db_session):
#     shipments = db_session.query(Shipment).all()
#     assert len(shipments) > 0
