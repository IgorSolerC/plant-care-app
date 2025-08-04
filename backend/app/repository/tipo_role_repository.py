from sqlalchemy.orm import Session
from app.models.enums import TipoRoleEnum
from app.models.tipo_role import TipoRole

def get_by_id(db: Session, *, role_id: TipoRoleEnum) -> TipoRole | None:
    """Busca uma role pelo id."""
    return db.query(TipoRole).filter(TipoRole.id == role_id.value).first()