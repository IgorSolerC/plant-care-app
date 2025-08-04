import random
import string
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.enums import TipoRoleEnum
from app.repository import grupo_repository, tipo_role_repository
from app.schemas.grupo import GrupoCreate

def create_invite_code() -> str:
    """Gera um código de convite aleatório de 6 caracteres."""
    characters = string.ascii_uppercase + string.digits
    
    return ''.join(random.choices(characters, k=6))

def create_default_group_for_user(db: Session, *, user: User) -> None:
    """
    Orquestra a criação de um grupo padrão para um usuário específico e o define como 'Admin'.
    
    Esta função assume que o `user` já foi adicionado à sessão (db.add(user))
    e que o commit será gerenciado pelo serviço que a chamou.
    
    Args:
        db (Session): A sessão do banco de dados.
        user (User): O objeto de usuário para o qual o grupo será criado.
    """
    # 1. Definir o nome do grupo
    first_name = user.full_name.split()[0] if user.full_name else "Meu"
    group_name = f"Grupo de {first_name}"
    
    # 2. Criar o grupo via repositório
    db_group = grupo_repository.create(db=db, group_in=GrupoCreate(nome=group_name, codigo_convite=create_invite_code()))
    db.flush()  # Garante que o db_group.id esteja disponível antes de criar a associação

    # 3. Obter a role "Admin"
    admin_role = tipo_role_repository.get_by_id(db=db, role_id=TipoRoleEnum.ADMIN)
    if not admin_role:
        raise Exception("Configuração do sistema inválida: A role 'Admin' não foi encontrada.")

    # 4. Associar o usuário ao grupo
    grupo_repository.add_user(db=db, user=user, group=db_group, role=admin_role)

    # Nota: O commit não é feito aqui. Ele será feito no serviço principal
    # que orquestra a transação completa (ex: user_service).
    