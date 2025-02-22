"""create user model v3

Revision ID: 5a2e66761346
Revises: 2af04fbb56f0
Create Date: 2025-02-19 19:54:12.996674

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a2e66761346'
down_revision: Union[str, None] = '2af04fbb56f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
