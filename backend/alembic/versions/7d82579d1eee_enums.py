"""Enums

Revision ID: 7d82579d1eee
Revises: ba3c2a921ace
Create Date: 2025-07-30 22:36:49.336741
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d82579d1eee'
down_revision = 'ba3c2a921ace'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ##  Inserção dos Dados em Cada Tabela (Data) ###

    # --- Dados para 'tipos_acao' ---
    tipos_acao_table = sa.table('tipos_acao', sa.column('id', sa.Integer), sa.column('nome', sa.String))
    op.bulk_insert(tipos_acao_table, [
        {'id': 1, 'nome': 'Pulado'},
        {'id': 2, 'nome': 'Feito'}
    ])

    # --- Dados para 'tipos_cronograma' ---
    tipos_cronograma_table = sa.table('tipos_cronograma', sa.column('id', sa.Integer), sa.column('nome', sa.String))
    op.bulk_insert(tipos_cronograma_table, [
        {'id': 1, 'nome': 'Flexível'},
        {'id': 2, 'nome': 'Fixo'}
    ])

    # --- Dados para 'tipos_fertilizante' ---
    tipos_fertilizante_table = sa.table('tipos_fertilizante', sa.column('id', sa.Integer), sa.column('nome', sa.String))
    op.bulk_insert(tipos_fertilizante_table, [
        {'id': 1, 'nome': 'Húmus de Minhoca'},
        {'id': 2, 'nome': 'NPK 10-10-10'}
    ])

    # --- Dados para 'tipos_luminosidade' ---
    tipos_luminosidade_table = sa.table('tipos_luminosidade', sa.column('id', sa.Integer), sa.column('nome', sa.String))
    op.bulk_insert(tipos_luminosidade_table, [
        {'id': 1, 'nome': 'Sombra'},
        {'id': 2, 'nome': 'Meia Sombra'},
        {'id': 3, 'nome': 'Luz Indireta'},
        {'id': 4, 'nome': 'Meio Sol'},
        {'id': 5, 'nome': 'Sol Pleno'}
    ])

    # --- Dados para 'tipos_rega' ---
    tipos_rega_table = sa.table('tipos_rega', sa.column('id', sa.Integer), sa.column('nome', sa.String))
    op.bulk_insert(tipos_rega_table, [
        {'id': 1, 'nome': 'Pouca'},
        {'id': 2, 'nome': 'Moderada'},
        {'id': 3, 'nome': 'Muita'}
    ])

    # --- Dados para 'tipos_role' ---
    tipos_role_table = sa.table('tipos_role', sa.column('id', sa.Integer), sa.column('nome', sa.String))
    op.bulk_insert(tipos_role_table, [
        {'id': 1, 'nome': 'Administrador'},
        {'id': 2, 'nome': 'Usuário'},
        {'id': 3, 'nome': 'Convidado'}
    ])

    # --- Dados para 'tipos_vento' ---
    tipos_vento_table = sa.table('tipos_vento', sa.column('id', sa.Integer), sa.column('nome', sa.String))
    op.bulk_insert(tipos_vento_table, [
        {'id': 1, 'nome': 'Indiferente'},
        {'id': 2, 'nome': 'Tolerante'},
        {'id': 3, 'nome': 'Sensível'},
        {'id': 4, 'nome': 'Necessita de Ventilação'}
    ])


def downgrade() -> None:
    op.execute('DELETE FROM tipos_vento;')
    op.execute('DELETE FROM tipos_role;')
    op.execute('DELETE FROM tipos_rega;')
    op.execute('DELETE FROM tipos_luminosidade;')
    op.execute('DELETE FROM tipos_fertilizante;')
    op.execute('DELETE FROM tipos_cronograma;')
    op.execute('DELETE FROM tipos_acao;')