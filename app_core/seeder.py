"""
Seeder para poblar la base de datos con datos sintéticos de ejemplo.

Uso básico:
    python seeder.py

Uso avanzado:
    python seeder.py --cantidad 20 --tenant tenant1

Parámetros:
    --cantidad N   Número de shipments por entidad (default: 10)
    --tenant T     Solo poblar datos para el tenant T (default: todos)
"""

import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.models import Base
from app.logic.datos_sinteticos import crear_datos_sinteticos, TENANTS

# Configura tu cadena de conexión aquí
DATABASE_URL = "sqlite:///./test.db"  # Cambia a tu base real si es necesario

def main():
    parser = argparse.ArgumentParser(description="Seeder de datos sintéticos para logística")
    parser.add_argument('--cantidad', type=int, default=10, help='Cantidad de shipments por entidad')
    parser.add_argument('--tenant', type=str, default=None, help='Tenant específico (opcional)')
    args = parser.parse_args()

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if args.tenant:
        if args.tenant not in TENANTS:
            print(f"Tenant '{args.tenant}' no está registrado. Opciones: {TENANTS}")
            return
        print(f"Cargando datos solo para tenant: {args.tenant}")
        crear_datos_sinteticos(db, n=args.cantidad, tenants=[args.tenant])
    else:
        print(f"Cargando datos para todos los tenants: {TENANTS}")
        crear_datos_sinteticos(db, n=args.cantidad)
    print("Datos sintéticos cargados exitosamente.")
    db.close()

if __name__ == "__main__":
    main()
