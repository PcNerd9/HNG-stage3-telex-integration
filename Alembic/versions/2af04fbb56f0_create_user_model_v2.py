"""create user model v2

Revision ID: 2af04fbb56f0
Revises: 0c8d2b4c6bbf
Create Date: 2025-02-19 19:53:03.104737

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2af04fbb56f0'
down_revision: Union[str, None] = '0c8d2b4c6bbf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
