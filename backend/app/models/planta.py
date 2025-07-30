from sqlalchemy import (
    Column, Integer, String, Text, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class Planta(Base):
    __tablename__ = "plantas"

    id = Column(Integer, primary_key=True, index=True)
    grupo_id = Column(Integer, ForeignKey("grupos.id"), nullable=False)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=True)
    foto_url = Column(String(255), nullable=True)
    
    tipo_rega_id = Column(Integer, ForeignKey("tipos_rega.id"), nullable=False)
    quantidade_ml_rega = Column(Integer, nullable=True)
    quantidade_dias_rega = Column(Integer, nullable=False)
    
    quantidade_dias_fertilizante = Column(Integer, nullable=True)
    tipo_fertilizante_id = Column(Integer, ForeignKey("tipos_fertilizante.id"), nullable=True)
    
    tipo_luminosidade_id = Column(Integer, ForeignKey("tipos_luminosidade.id"), nullable=False)
    tipo_vento_id = Column(Integer, ForeignKey("tipos_vento.id"), nullable=False)
    tipo_cronograma_id = Column(Integer, ForeignKey("tipos_cronograma.id"), nullable=False)

    data_cadastro = Column(DateTime, server_default=func.now(), nullable=False)
    data_atualizacao = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    grupo = relationship("Grupo", back_populates="plantas")
    tipo_rega = relationship("TipoRega")
    tipo_fertilizante = relationship("TipoFertilizante")
    tipo_luminosidade = relationship("Luminosidade")
    tipo_vento = relationship("TipoVento")
    tipo_cronograma = relationship("TipoCronograma")
    logs_atividade = relationship("LogAtividade", back_populates="planta")