"""added __table_args__ to join table

Revision ID: 3f61c3a017b8
Revises: 52f3a298acb7
Create Date: 2023-09-07 09:49:54.320820

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f61c3a017b8'
down_revision: Union[str, None] = '52f3a298acb7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###