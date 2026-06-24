from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import engine, Base

# Importar todos los modelos para que SQLAlchemy los registre
from app.models import Empresa, Usuario, Ubicacion, Criticidad, Maquinaria, EspecificacionTecnica, DocumentoEquipo, PlanMantenimiento, OrdenTrabajo

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Todo lo que va aquí se ejecuta al ARRANCAR el servidor
    Base.metadata.create_all(bind=engine)
    print("✅ Conexión a base de datos exitosa")
    yield
    # Todo lo que va después del yield se ejecuta al APAGAR el servidor

app = FastAPI(title="CMMS API", version="1.0.0", lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "API de Gestión de Mantenimiento funcionando ✅"}