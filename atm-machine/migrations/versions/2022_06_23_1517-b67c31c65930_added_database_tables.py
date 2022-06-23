"""Added Database Tables

Revision ID: b67c31c65930
Revises: 
Create Date: 2022-06-23 15:17:11.681773

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b67c31c65930'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('email', sa.String(length=256), nullable=False),
                    sa.Column('phone_number', sa.String(length=256), nullable=False),
                    sa.Column('full_name', sa.String(length=256), nullable=False),
                    sa.Column('created_by', sa.String(length=256), nullable=False),
                    sa.Column('created_on', sa.DateTime(timezone=True), nullable=False),
                    sa.Column('modified_by', sa.String(length=256), nullable=False),
                    sa.Column('modified_on', sa.DateTime(timezone=True), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    schema='info'
                    )
    op.create_index('idx_email_user', 'user', ['email'], unique=False, schema='info')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_email_user', table_name='user', schema='info')
    op.drop_table('user', schema='info')
    # ### end Alembic commands ###