from sqlalchemy import Column, Integer, String
from .base import Base

class TipoRega(Base):
    __tablename__ = "tipos_rega"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, nullable=False)
