"""likers

Revision ID: 6342c6105818
Revises: 71571bf0df5e
Create Date: 2020-05-25 15:39:29.499859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6342c6105818'
down_revision = '71571bf0df5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likers',
    sa.Column('liker_id', sa.Integer(), nullable=True),
    sa.Column('liked_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['liked_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['liker_id'], ['post.id'], )
    )
    op.create_table('post_like',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_like')
    op.drop_table('likers')
    # ### end Alembic commands ###
