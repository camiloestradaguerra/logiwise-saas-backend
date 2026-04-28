# Seeder y Datos Sintéticos para Desarrollo y Pruebas

Este proyecto incluye un script seeder y fixtures para poblar la base de datos con datos sintéticos realistas, facilitando el desarrollo, pruebas y demos.

## Uso del Seeder

El seeder permite poblar la base de datos de desarrollo/demo con datos sintéticos para múltiples tenants y entidades.

### Ejecución básica

Pobla la base de datos con datos para todos los tenants y 10 shipments por entidad:

```
python nuevaflo_core/seeder.py
```

### Parámetros avanzados

- `--cantidad N`  
  Especifica la cantidad de shipments por entidad (por defecto: 10).
- `--tenant TENANT_ID`  
  Solo pobla datos para el tenant indicado (por defecto: todos los tenants).

Ejemplos:

- Poblar 20 shipments por entidad para todos los tenants:
  ```
  python nuevaflo_core/seeder.py --cantidad 20
  ```
- Poblar solo para un tenant específico:
  ```
  python nuevaflo_core/seeder.py --tenant tenant1
  ```

## Uso en Pruebas Automatizadas (pytest)

El fixture `db_session` en `tests/conftest.py` inicializa una base de datos en memoria y la puebla con datos sintéticos para cada test, asegurando aislamiento y limpieza.

Ejemplo de uso en un test:

```
def test_shipment_count(db_session):
    shipments = db_session.query(Shipment).all()
    assert len(shipments) > 0
```

## Buenas Prácticas

- Usa el seeder solo en entornos de desarrollo o demo, nunca en producción.
- Los datos sintéticos se regeneran cada vez que ejecutas el seeder o los tests.
- Para mantener los datos de prueba consistentes y aislados, cada test usa una base de datos en memoria.
- Puedes modificar las listas de ejemplo en `nuevaflo_core/app/logic/datos_sinteticos.py` para personalizar los datos generados.

---

¿Dudas o sugerencias? ¡Contribuye o abre un issue!
