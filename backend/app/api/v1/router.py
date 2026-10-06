from fastapi import APIRouter, HTTPException, status
from backend.app.schemas.user import UserCreate, UserResponse
from backend.app.services.user_service import UserService

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    """
    Crea un nuevo usuario en la base de datos.
    """
    service = UserService()
    # Pydantic v2: pasar el objeto directamente, no user.dict()
    return service.create_user(user)
