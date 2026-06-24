"""add is_active to students

Revision ID: 34eb8646fcb1
Revises: 07ffc2669606
Create Date: 2026-06-24 20:02:04.128234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '34eb8646fcb1'
down_revision: Union[str, Sequence[str], None] = '07ffc2669606'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.add_column('students', sa.Column('is_active', sa.Boolean(), nullable=True))
    


def downgrade() -> None:
    
    op.drop_column('students', 'is_active')
    