from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.v1.router import router as api_v1_router
from backend.app.api.v2.router import router as api_v2_router
from backend.app.core.database import engine
from backend.app.models import Base

# Inicializar tablas de la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fuerza Base App", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Fuerza Base App iniciado con éxito", "status": "online"}

app.include_router(api_v1_router, prefix="/api/v1")
app.include_router(api_v2_router, prefix="/api/v2")
