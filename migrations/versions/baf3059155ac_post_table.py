"""post table

Revision ID: baf3059155ac
Revises: 
Create Date: 2019-08-19 20:50:32.306320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baf3059155ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('user_name', sa.String(length=64), nullable=True),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.Column('text', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###