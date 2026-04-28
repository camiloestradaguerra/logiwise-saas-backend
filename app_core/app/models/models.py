from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime, Numeric
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()

class ShipmentMode(enum.Enum):
    AEREO = "aéreo"
    MARITIMO = "marítimo"
    TERRESTRE = "terrestre"

class ShipmentState(enum.Enum):
    DRAFT = "Draft"
    QUOTED = "Quoted"
    BOOKED = "Booked"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    INVOICED = "Invoiced"

class Entity(Base):
    __tablename__ = "entities"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, nullable=False)  # Multi-tenant
    name = Column(String, nullable=False)
    entity_type = Column(String, nullable=False)  # cliente/proveedor
    tax_id = Column(String)
    contact_name = Column(String)
    contact_email = Column(String)
    contact_phone = Column(String)
    shipments = relationship("Shipment", back_populates="client")

class Shipment(Base):
    __tablename__ = "shipments"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, nullable=False)  # Multi-tenant
    mode = Column(Enum(ShipmentMode), nullable=False)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    cargo_type = Column(String, nullable=False)  # FCL/LCL, tipo de carga
    state = Column(Enum(ShipmentState), default=ShipmentState.DRAFT)
    currency = Column(String, nullable=False)  # USD, CLP, COP, etc.
    weight_kg = Column(Float)
    volume_cbm = Column(Float)
    client_id = Column(Integer, ForeignKey("entities.id"))
    client = relationship("Entity", back_populates="shipments")
    quotes = relationship("Quote", back_populates="shipment")
    documents = relationship("Document", back_populates="shipment")

class Quote(Base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, nullable=False)  # Multi-tenant
    shipment_id = Column(Integer, ForeignKey("shipments.id"))
    buy_rate = Column(Numeric(precision=12, scale=2), nullable=False)
    sell_rate = Column(Numeric(precision=12, scale=2), nullable=False)
    currency = Column(String, nullable=False)
    taxes = Column(Numeric(precision=12, scale=2), default=0)
    created_at = Column(DateTime)
    shipment = relationship("Shipment", back_populates="quotes")

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, nullable=False)  # Multi-tenant
    shipment_id = Column(Integer, ForeignKey("shipments.id"))
    doc_type = Column(String, nullable=False)  # BL, AWB, Factura, etc.
    file_path = Column(String, nullable=False)
    uploaded_at = Column(DateTime)
    shipment = relationship("Shipment", back_populates="documents")
