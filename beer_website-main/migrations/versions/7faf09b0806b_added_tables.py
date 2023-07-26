"""added tables

Revision ID: 7faf09b0806b
Revises: e33b84ad9b5d
Create Date: 2023-05-30 17:41:15.317555

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7faf09b0806b'
down_revision = ''
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    op.create_table('brands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('colors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('color_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cuttings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cutting_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('materials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('material_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stone_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('styles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('style_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weavings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weaving_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'cart')
    op.create_table('orders',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('products_id', postgresql.ARRAY(sa.INTEGER()), autoincrement=False, nullable=False),
    sa.Column('status', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('address', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('order_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='orders_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='orders_pkey')
    )
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('role_name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('role_permissions', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    op.drop_table('weavings')
    op.drop_table('styles')
    op.drop_table('stones')
    op.drop_table('materials')
    op.drop_table('cuttings')
    op.drop_table('colors')
    op.drop_table('categories')
    op.drop_table('brands')
    # ### end Alembic commands ###
