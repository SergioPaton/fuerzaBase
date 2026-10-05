from fastapi import HTTPException, status
from backend.app.schemas.user import UserCreate, UserResponse
from backend.app.models.user import User
from backend.app.core.database import get_db
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    @staticmethod
    def create_user(user_data: UserCreate) -> UserResponse:
        """
        Crea un nuevo usuario con validación de existencia y hashing de contraseña.
        """
        db = next(get_db())
        try:
            # Verificar si el usuario ya existe
            existing = db.query(User).filter(User.email == user_data.email).first()
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El usuario ya existe"
                )

            # Hashear la contraseña
            hashed_password = pwd_context.hash(user_data.password)

            # Crear el usuario
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
            return UserResponse(**user.__dict__)
        except Exception as e:
            db.rollback()
            raise e
