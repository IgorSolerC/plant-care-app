from sqlalchemy import Column, Integer, String
from .base import Base

class TipoLuminosidade(Base):
    __tablename__ = "tipos_luminosidade"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, nullable=False)