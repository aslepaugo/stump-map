"""empty message

Revision ID: 20c0b7e207cb
Revises: e3398ebd622b
Create Date: 2020-11-04 19:04:09.050292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20c0b7e207cb'
down_revision = 'e3398ebd622b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stump_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('stump', sa.Column('created', sa.DateTime(), nullable=True))
    op.execute("UPDATE stump SET created = '1900-01-01 00:00:00'")
    op.alter_column('stump', 'created', nullable=False)
    op.add_column('stump', sa.Column('stump_status_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'stump', 'stump_status', ['stump_status_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stump', type_='foreignkey')
    op.drop_column('stump', 'stump_status_id')
    op.drop_column('stump', 'created')
    op.drop_table('stump_status')
    # ### end Alembic commands ###