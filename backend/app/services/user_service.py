from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import httpx

from app.core.config import settings
from app.models.user import User
import app.schemas.user as user_schemas

from app.services import grupo_service
from app.repository import user_repository

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def registrar_user_com_grupo_padrao(db: Session, user_in: user_schemas.UserCreate):
    """
    Orquestra a criação de um novo usuário e seu grupo padrão.
    """
    # 1. Criar o usuário via repositório
    db_user = user_repository.create(db=db, user_in=user_in)
    db.flush()  # Garante que o ID do usuário esteja disponível para o próximo passo
    
    # 2. Chamar o serviço de grupo para criar o grupo padrão
    grupo_service.create_default_group_for_user(db=db, user=db_user)
    
    # 3. Commit da transação
    db.commit()
    db.refresh(db_user)

    return db_user

async def get_or_create_user_from_google(db: Session, authorization_code: str):
    """
    Orquestra a autenticação ou registro de um usuário via Google.
    - Se o usuário é novo, cria o usuário e seu grupo padrão.
    - Se o usuário já existe, apenas o retorna ou vincula a conta Google.
    """
    # 1. Comunicação com a API do Google para obter informações do usuário
    try:
        token_url = "https://oauth2.googleapis.com/token"
        token_data = {
            "code": authorization_code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }
        
        async with httpx.AsyncClient() as client:
            token_response = await client.post(token_url, data=token_data)
            token_response.raise_for_status()
            access_token = token_response.json().get("access_token")

            userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
            headers = {"Authorization": f"Bearer {access_token}"}
            userinfo_response = await client.get(userinfo_url, headers=headers)
            userinfo_response.raise_for_status()
            user_info = userinfo_response.json()
            
    except httpx.HTTPStatusError as e:
        # Erro na comunicação com o Google
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erro ao validar o código de autorização com o Google: {e.response.text}"
        )

    # 2. Lógica de negócio usando a camada de repositório
    user = user_repository.get_by_email(db, email=user_info["email"])

    if not user:
        # CASO 1: Usuário é completamente novo. Criar usuário e grupo padrão.
        new_user = user_repository.create_from_google(
            db,
            email=user_info["email"],
            full_name=user_info.get("name"),
            google_id=user_info["id"]
        )
        db.flush()

        # Lógica de criação de grupo padrão
        grupo_service.create_default_group_for_user(db=db, user=new_user)

        user = new_user

    elif user.google_id is None:
        # CASO 2: Usuário existe, apenas vincular conta Google.
        user_repository.link_google_account(db, user=user, google_id=user_info["id"])
    
    # CASO 3: Usuário já existe e já tem conta Google vinculada. Nenhuma ação é necessária.
    
    # 3. Finalizar a transação
    db.commit()
    db.refresh(user)
    
    return user


def get_all_users(db: Session):
    """
    Retrieves all users from the database.
    """
    return db.query(User).all()