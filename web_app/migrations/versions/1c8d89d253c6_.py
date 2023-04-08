"""empty message

Revision ID: 1c8d89d253c6
Revises: 9ce2fea93f1b
Create Date: 2023-04-04 11:54:51.214583

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "1c8d89d253c6"
down_revision = "9ce2fea93f1b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("Profiles", schema=None) as batch_op:
        batch_op.alter_column(
            "total_searched_cars", existing_type=sa.INTEGER(), nullable=True
        )
        batch_op.alter_column(
            "registration_date", existing_type=postgresql.TIMESTAMP(), nullable=True
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("Profiles", schema=None) as batch_op:
        batch_op.alter_column(
            "registration_date", existing_type=postgresql.TIMESTAMP(), nullable=False
        )
        batch_op.alter_column(
            "total_searched_cars", existing_type=sa.INTEGER(), nullable=False
        )

    # ### end Alembic commands ###
