from sqlalchemy import (
    Column, Integer, String, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class Grupo(Base):
    __tablename__ = "grupos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    codigo_convite = Column(String(255), unique=True, nullable=False)
    data_cadastro = Column(DateTime, server_default=func.now())

    plantas = relationship("Planta", back_populates="grupo")
    usuarios_associados = relationship("GrupoUser", back_populates="grupo")