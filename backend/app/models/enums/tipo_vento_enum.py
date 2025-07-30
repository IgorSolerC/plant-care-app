import enum

class TipoVentoEnum(enum.Enum):
    """Tolerância da planta a ambientes com vento."""
    INDIFERENTE = 1
    TOLERANTE = 2
    SENSIVEL = 3
    NECESSITA = 4