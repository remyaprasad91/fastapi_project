"""create posts table

Revision ID: 7e5818a7ac84
Revises: 
Create Date: 2025-12-26 18:09:08.826833

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e5818a7ac84'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('title', sa.String, nullable=False)
        )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass