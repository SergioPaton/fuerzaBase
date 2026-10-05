from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from backend.app.schemas.user import UserCreate, UserResponse
from backend.app.services.user_service import UserService


router = APIRouter()


@router.post("/users/")
def create_user(user: UserCreate):
    """
    Crea un nuevo usuario en la base de datos.
    """
    service = UserService()
    user_response = service.create_user(user.dict())
    return user_response
