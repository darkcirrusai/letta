"""add column to tools table to contain function return limit return_char_limit

Revision ID: a91994b9752f
Revises: e1a625072dbf
Create Date: 2024-12-09 18:27:25.650079

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from letta.constants import FUNCTION_RETURN_CHAR_LIMIT

# revision identifiers, used by Alembic.
revision: str = "a91994b9752f"
down_revision: Union[str, None] = "e1a625072dbf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("tools", sa.Column("return_char_limit", sa.Integer(), nullable=True))

    # Populate `return_char_limit` column
    op.execute(
        f"""
        UPDATE tools
        SET return_char_limit = {FUNCTION_RETURN_CHAR_LIMIT}
        """
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("tools", "return_char_limit")
    # ### end Alembic commands ###
