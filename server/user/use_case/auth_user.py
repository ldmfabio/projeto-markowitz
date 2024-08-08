from sqlalchemy.orm import Session 
from sqlalchemy.exc import IntegrityError
from db.models import UserModel
from server.schemas import User
from passlib.context import CryptContext
from fastapi import HTTPException, status


crypt_context = CryptContext(schemes=["sha256_crypt"])


class UserUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session   

    def create_user(self, user: User):
        user_model = UserModel(
            name=user.name,
            email=user.email,
            password=crypt_context.hash(user.password)
        )
        try:
            self.db_session.add(user_model)
            self.db_session.commit()
            self.db_session.refresh(user_model)
            return user_model
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists"
            )