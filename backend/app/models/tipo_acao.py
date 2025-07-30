from sqlalchemy import Column, Integer, String
from .base import Base

class TipoAcao(Base):
    __tablename__ = "tipos_acao"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, nullable=False)