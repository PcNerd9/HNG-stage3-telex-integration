"""initials create user model

Revision ID: 0c8d2b4c6bbf
Revises: 45252500f4a9
Create Date: 2025-02-19 19:45:44.916324

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c8d2b4c6bbf'
down_revision: Union[str, None] = '45252500f4a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
