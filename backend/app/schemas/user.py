from pydantic import BaseModel, EmailStr
from typing import List, Optional

from app.schemas.grupo_user import GrupoUserAssociacaoInfo

# --- Token Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# --- User Schemas ---
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

# --- Google Login Schema ---
class GoogleLoginRequest(BaseModel):
    code: str # The authorization code from the Angular frontend

class UserReadComGrupos(UserRead):
    grupos_associados: List[GrupoUserAssociacaoInfo] = []