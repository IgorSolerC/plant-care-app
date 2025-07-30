import enum

class TipoLuminosidadeEnum(enum.Enum):
    """Níveis de luminosidade que a planta necessita."""
    SOMBRA = 1
    MEIA_SOMBRA = 2
    LUZ_INDIRETA = 3
    MEIO_SOL = 4
    SOL_PLENO = 5
    
    