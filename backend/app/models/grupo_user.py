from sqlalchemy import (
    Column, ForeignKey, Integer, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class GrupoUser(Base):
    __tablename__ = "grupos_users"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    grupo_id = Column(Integer, ForeignKey("grupos.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("tipos_role.id"), nullable=False)
    data_cadastro = Column(DateTime, server_default=func.now())

    usuario = relationship("User", back_populates="grupos_associados")
    grupo = relationship("Grupo", back_populates="usuarios_associados")
    role = relationship("TipoRole")