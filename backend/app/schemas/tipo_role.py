# Schema para exibir a role do usuário no grupo
from pydantic import BaseModel

class RoleInfo(BaseModel):
    nome: str

    class Config:
        from_attributes = True
