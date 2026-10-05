from fastapi import FastAPI
from backend.app.api.v1.router import router as api_router
from backend.app.core.database import engine, SessionLocal, Base

app = FastAPI(title="Fuerza Base App")

@app.get("/")
def read_root():
    return {"message": "Fuerza Base App iniciado"}

app.include_router(api_router, prefix="/api/v1")
