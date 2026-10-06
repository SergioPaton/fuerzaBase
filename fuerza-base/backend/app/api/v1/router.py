from fastapi import APIRouter, HTTPException, status
from backend.app.schemas.user import UserCreate, UserResponse
from backend.app.services.user_service import UserService

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok", "version": "v1"}

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    """
    Crea un nuevo usuario en la base de datos.
    """
    service = UserService()
    return service.create_user(user)
