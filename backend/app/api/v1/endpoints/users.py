from typing import Annotated
from fastapi import APIRouter, Depends
from app.auth import dependencies
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import user_service as user_service

from app.schemas import user as user_schemas
from app.models.user import User

router = APIRouter()

@router.get("/me", response_model=user_schemas.UserReadComGrupos)
def read_users_me(current_user: Annotated[User, Depends(dependencies.get_current_active_user)]):
    return current_user

@router.get("/", response_model=list[user_schemas.UserRead], tags=["users"])
def read_all_users(
    current_user: Annotated[User, Depends(dependencies.get_current_active_user)],
    db: Session = Depends(get_db),
):
    """
    Retrieve all users.
    This is a protected endpoint that requires authentication.
    """
    users = user_service.get_all_users(db=db)
    return users