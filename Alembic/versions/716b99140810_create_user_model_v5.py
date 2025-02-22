"""create user model v5

Revision ID: 716b99140810
Revises: ca89b76c57a8
Create Date: 2025-02-19 20:01:48.507984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '716b99140810'
down_revision: Union[str, None] = 'ca89b76c57a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
