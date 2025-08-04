from pydantic import BaseModel

from app.schemas.grupo import GrupoRead 
from app.schemas.tipo_role import RoleInfo

# Schema para representar a associação completa (Grupo + Role)
class GrupoUserAssociacaoInfo(BaseModel):
    grupo: GrupoRead
    role: RoleInfo

    class Config:
        from_attributes = True

