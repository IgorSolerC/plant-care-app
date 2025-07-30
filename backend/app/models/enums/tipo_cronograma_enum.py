import enum

class TipoCronogramaEnum(enum.Enum):
    """Comportamento do agendamento das tarefas da planta."""
    FLEXIVEL = 1
    FIXO = 2