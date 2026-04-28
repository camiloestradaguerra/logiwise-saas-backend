from fastapi import FastAPI
from app.api.routes import router as api_router
from app.api.auth import router as auth_router

app = FastAPI(title="Logistic Project API")

# Registrar routers
app.include_router(api_router)
app.include_router(auth_router)

# Puedes agregar middlewares, eventos de startup/shutdown, etc. aquí

# Ejemplo de endpoint raíz
@app.get("/")
def root():
    return {"msg": "API de logística en funcionamiento"}
