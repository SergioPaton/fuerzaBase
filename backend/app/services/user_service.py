from fastapi import HTTPException, status
from backend.app.schemas.user import UserCreate, UserResponse
from backend.app.models.user import User
from backend.app.core.database import SessionLocal
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    @staticmethod
    def create_user(user_data: UserCreate) -> UserResponse:
        db = SessionLocal()
        try:
            existing = db.query(User).filter(User.email == user_data.email).first()
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El usuario ya existe"
                )

            hashed_password = pwd_context.hash(user_data.password)

            user = User(
                first_name=user_data.first_name,
                last_name=user_data.last_name,
                email=user_data.email,
                hashed_password=hashed_password,
                role=user_data.role
            )
            db.add(user)
            db.commit()
            db.refresh(user)

            return UserResponse(
                id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                role=user.role,
                created_at=user.created_at
            )
        except HTTPException:
            db.rollback()
            raise
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )
        finally:
            db.close()
