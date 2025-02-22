"""added failed_loggin_Attempt model

Revision ID: 4ea03059f03e
Revises: 716b99140810
Create Date: 2025-02-20 02:04:08.816351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ea03059f03e'
down_revision: Union[str, None] = '716b99140810'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
