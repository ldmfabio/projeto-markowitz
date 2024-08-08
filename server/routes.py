from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from server.user.use_case.auth_user import UserUseCases
from server.depends import get_db_session
from server.schemas import User

router = APIRouter(prefix="/api")

@router.post("/register")
def user_register(user: User, db_session: Session = Depends(get_db_session)):
    uc.UserUseCases(db_session=db_session)
    uc.create_user(user=user)
    
    return Response(status_code=201, content="User created")
