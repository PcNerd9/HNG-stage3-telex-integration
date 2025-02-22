"""create user model v4

Revision ID: ca89b76c57a8
Revises: 5a2e66761346
Create Date: 2025-02-19 19:57:41.262455

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca89b76c57a8'
down_revision: Union[str, None] = '5a2e66761346'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
