"""Add password_hash

Revision ID: 3695279740ec
Revises: 8f049dfc4b18
Create Date: 2019-04-23 11:52:12.627794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3695279740ec'
down_revision = '8f049dfc4b18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
