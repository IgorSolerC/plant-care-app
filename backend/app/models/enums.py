from enum import IntEnum

class TipoAcaoEnum(IntEnum):
    """Tipos de ações registradas nos logs."""
    PULADO = 1
    FEITO = 2

class TipoCronogramaEnum(IntEnum):
    """Comportamento do agendamento das tarefas da planta."""
    FLEXIVEL = 1
    FIXO = 2

class TipoFertilizanteEnum(IntEnum):
    """Tipos de fertilizantes."""
    HUMUS_DE_MINHOCA = 1
    NPK_10_10_10 = 2

class TipoLuminosidadeEnum(IntEnum):
    """Níveis de luminosidade que a planta necessita."""
    SOMBRA = 1
    MEIA_SOMBRA = 2
    LUZ_INDIRETA = 3
    MEIO_SOL = 4
    SOL_PLENO = 5

class TipoRegaEnum(IntEnum):
    """Categorias para a quantidade de água na rega."""
    POUCA = 1
    MODERADA = 2
    MUITA = 3

class TipoRoleEnum(IntEnum):
    """Tipos de roles de usuário no sistema."""
    ADMIN = 1
    USER = 2
    GUEST = 3

class TipoVentoEnum(IntEnum):
    """Tolerância da planta a ambientes com vento."""
    INDIFERENTE = 1
    TOLERANTE = 2
    SENSIVEL = 3
    NECESSITA = 4