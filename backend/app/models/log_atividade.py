from sqlalchemy import (
    Column, Integer, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class LogAtividade(Base):
    __tablename__ = "logs_atividade"

    id = Column(Integer, primary_key=True, index=True)
    planta_id = Column(Integer, ForeignKey("plantas.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tipo_acao_id = Column(Integer, ForeignKey("tipos_acao.id"))
    data_atividade = Column(DateTime, server_default=func.now())

    planta = relationship("Planta", back_populates="logs_atividade")
    usuario = relationship("User", back_populates="atividades")
    tipo_acao = relationship("TipoAcao")
