"""init migration

Revision ID: fe7200e4cbbf
Revises: 
Create Date: 2024-07-31 10:36:38.163717

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'fe7200e4cbbf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('designers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('payment', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('works',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('customer', sa.String(), nullable=False),
                    sa.Column('headline', sa.String(), nullable=False),
                    sa.Column('value', sa.Integer(), nullable=False),
                    sa.Column('date_of_payment', sa.DateTime(), nullable=True),
                    sa.Column('designer_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['designer_id'], ['designers.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('works')
    op.drop_table('designers')
    op.drop_table('admins')
    # ### end Alembic commands ###
