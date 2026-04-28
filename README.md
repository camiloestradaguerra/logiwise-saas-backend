# logiwise-saas-backend

Backend SaaS logístico multi-tenant para Latinoamérica

---

## Descripción

Este proyecto es un backend modular y escalable para gestión logística, adaptado a las necesidades de Latinoamérica. Incluye:
- FastAPI (Python 3.11+)
- Multi-tenant (SaaS)
- Autenticación y roles (JWT)
- CRUD de Shipments, Quotes, Entities y Documents
- Conversión de unidades y multimoneda
- Seeders y datos sintéticos
- Docker y CI/CD
- Pruebas automatizadas (pytest)

## Instalación rápida

```sh
python -m venv venv
venv\Scripts\activate  # En Windows
# source venv/bin/activate  # En Mac/Linux
pip install --upgrade pip
pip install -r requirements.txt
```

## Uso con Docker

```sh
docker build -t logistic-fastapi .
docker run -d -p 8000:8000 --name logistic-fastapi logistic-fastapi uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Pruebas

```sh
pytest tests/
```

## Documentación
- [docs/](docs/) para glosario y detalles técnicos.

---

© 2026 camiloestradaguerra