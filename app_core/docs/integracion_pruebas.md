# Plan de Integración y Pruebas

Este documento describe cómo integrar los módulos desarrollados y cómo realizar pruebas unitarias y de integración para asegurar el correcto funcionamiento del sistema.

## 1. Integración de la Aplicación FastAPI

- Crea un archivo `main.py` en la raíz de `app/`.
- Importa y monta los routers de los endpoints definidos en `app/api/routes.py`.
- Configura la base de datos y las dependencias necesarias.

## 2. Estructura de Pruebas

- Crea una carpeta `tests/` en la raíz del proyecto.
- Dentro de `tests/`, crea archivos de prueba para cada módulo principal:
  - `test_cotizacion.py` (cálculo de margen)
  - `test_unidades_moneda.py` (conversión de unidades y moneda)
  - `test_shipment_manager.py` (gestión de estados)
  - `test_document_manager.py` (gestión de documentos)

## 3. Ejemplo de Pruebas con pytest

### test_cotizacion.py
```python
from app.logic.cotizacion import calcular_margen_envio

def test_calcular_margen_envio():
    profit, margen = calcular_margen_envio(1000, 1500, iva=0.19, retencion=0.015)
    assert round(profit, 2) == 485.0
    assert round(margen, 2) == 32.33
```

### test_unidades_moneda.py
```python
from app.logic.unidades_moneda import kilos_a_libras, cbm_a_peso_volumetrico, convertir_moneda

def test_kilos_a_libras():
    assert round(kilos_a_libras(10), 2) == 22.05

def test_cbm_a_peso_volumetrico():
    assert cbm_a_peso_volumetrico(2, modo="aereo") == 334

def test_convertir_moneda():
    assert convertir_moneda(100, 950) == 95000
```

## 4. Ejecución de Pruebas

- Instala pytest si no lo tienes: `pip install pytest`
- Ejecuta las pruebas desde la raíz del proyecto:
  ```bash
  pytest
  ```

## 5. Verificación de Integración

- Lanza la app FastAPI (`main.py`) y verifica que los endpoints estén disponibles en `/docs` (Swagger UI).
- Realiza pruebas manuales de integración usando Swagger o herramientas como Postman.

---

Este plan asegura que todos los módulos estén correctamente integrados y validados mediante pruebas automatizadas y manuales.
