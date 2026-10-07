from fastapi import APIRouter, HTTPException, status, Depends
from backend.app.core.database import get_db
from backend.app.use_cases.create_user import CreateUserUseCase
from backend.app.db.gateways.sqlalchemy_user_gateway import SQLAlchemyUserGateway
from backend.app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok", "version": "v1"}

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db=Depends(get_db)):
    try:
        gateway = SQLAlchemyUserGateway(db)
        entity = CreateUserUseCase(gateway).execute(user)
        return UserResponse(id=entity.id, first_name=entity.first_name, last_name=entity.last_name, email=entity.email, role=entity.role, created_at=entity.created_at)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
