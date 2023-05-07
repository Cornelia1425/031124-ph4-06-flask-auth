"""empty message

Revision ID: d077601a49a9
Revises: ab72cc87dcb4
Create Date: 2023-05-07 11:37:03.630041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd077601a49a9'
down_revision = 'ab72cc87dcb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###