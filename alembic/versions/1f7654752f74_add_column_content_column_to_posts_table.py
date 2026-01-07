"""add column content column to posts table

Revision ID: 1f7654752f74
Revises: 7e5818a7ac84
Create Date: 2025-12-26 19:24:30.165790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f7654752f74'
down_revision: Union[str, Sequence[str], None] = '7e5818a7ac84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
