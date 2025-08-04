from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.auth import security
import app.services.user_service as user_service
import app.schemas.user as user_schemas


router = APIRouter()

@router.post("/register", response_model=user_schemas.UserRead, status_code=status.HTTP_201_CREATED)
def registrar_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado")
    return user_service.registrar_user_com_grupo_padrao(db=db, user_in=user)

@router.post("/login", response_model=user_schemas.Token)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    user = user_service.get_user_by_email(db, email=form_data.username)
    if not user or user.hashed_password is None or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/google/login", response_model=user_schemas.Token)
async def google_login(
    request: user_schemas.GoogleLoginRequest,
    db: Session = Depends(get_db)
):
    try:
        user = await user_service.get_or_create_user_from_google(db, request.code)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Login Google falhou: {e}")

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não foi possível validar as credenciais do Google")

    access_token = security.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

