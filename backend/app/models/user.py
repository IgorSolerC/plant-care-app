from typing import List, Optional
from sqlalchemy import String
from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.log_atividade import LogAtividade
from app.models.grupo_user import GrupoUser

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[Optional[str]] = mapped_column(String(100), index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    hashed_password: Mapped[Optional[str]] = mapped_column(String(255), nullable=True) # Nullable for Google-only users
    google_id: Mapped[Optional[str]] = mapped_column(String(255), unique=True, nullable=True) # For Google OAuth users
    is_active: Mapped[bool] = mapped_column(default=True)
    
    atividades: Mapped[List["LogAtividade"]] = relationship(back_populates="usuario")
    grupos_associados: Mapped[List["GrupoUser"]] = relationship(back_populates="usuario")