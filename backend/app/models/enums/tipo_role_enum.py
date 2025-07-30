import enum

class TipoRoleEnum(enum.Enum):
    """Tipos de papéis de usuário no sistema."""
    ADMIN = 1
    USER = 2
    GUEST = 3