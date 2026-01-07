"""add users table

Revision ID: 7af3f81f9ea0
Revises: 1f7654752f74
Create Date: 2025-12-26 19:58:22.252482

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7af3f81f9ea0'
down_revision: Union[str, Sequence[str], None] = '1f7654752f74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))
    )   
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
