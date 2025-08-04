from pydantic import BaseModel

class GrupoBase(BaseModel):
    nome: str

class GrupoCreate(GrupoBase):
    pass

class GrupoRead(GrupoBase):
    id: int
    codigo_convite: str

    class Config:
        from_attributes = True
