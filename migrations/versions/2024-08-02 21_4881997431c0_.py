"""empty message

Revision ID: 4881997431c0
Revises: 8ac02debbb45
Create Date: 2024-08-02 21:39:13.652197

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4881997431c0'
down_revision: Union[str, None] = '8ac02debbb45'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('works_designer_id_fkey', 'works', type_='foreignkey')
    op.create_foreign_key(None, 'works', 'designers', ['designer_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'works', type_='foreignkey')
    op.create_foreign_key('works_designer_id_fkey', 'works', 'designers', ['designer_id'], ['id'])
    # ### end Alembic commands ###
