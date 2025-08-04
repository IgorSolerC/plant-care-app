from sqlalchemy.orm import Session
from app.models.user import User
from app.models.grupo import Grupo
from app.models.grupo_user import GrupoUser
from app.models.tipo_role import TipoRole
from app.schemas.grupo import GrupoCreate
 
def create(db: Session, *, group_in: GrupoCreate) -> Grupo:
    """Cria um novo grupo no banco de dados."""
    db_group = Grupo(
        nome=group_in.nome,
        codigo_convite=group_in.codigo_convite 
    )
    db.add(db_group)
    return db_group

def add_user(db: Session, *, user: User, group: Grupo, role: TipoRole):
    """Cria a associação entre um usuário e um grupo."""
    association = GrupoUser(usuario=user, grupo=group, role=role)
    db.add(association)
    return association