"""columns for profile added

Revision ID: 3c16ee42b2a4
Revises: 61be7df1d15a
Create Date: 2020-09-30 17:16:03.399059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c16ee42b2a4'
down_revision = '61be7df1d15a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('blogpost_id', sa.Integer(), nullable=True))
    op.alter_column('comments', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('comments_post_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'blogposts', ['blogpost_id'], ['id'])
    op.drop_column('comments', 'post_id')
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    op.add_column('comments', sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_post_id_fkey', 'comments', 'blogposts', ['post_id'], ['id'])
    op.alter_column('comments', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('comments', 'blogpost_id')
    # ### end Alembic commands ###
