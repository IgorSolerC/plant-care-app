import enum

class SchedulingBehaviorEnum(enum.Enum):
    """Comportamento do agendamento das tarefas da planta."""
    FLEXIVEL = 0
    FIXO = 1