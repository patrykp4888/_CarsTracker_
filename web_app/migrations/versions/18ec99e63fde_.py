"""empty message

Revision ID: 18ec99e63fde
Revises: 84a33bb86895
Create Date: 2023-04-08 14:29:13.966175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "18ec99e63fde"
down_revision = "84a33bb86895"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "Brands",
        sa.Column("brand_id", sa.Integer(), nullable=False),
        sa.Column("brand", sa.String(length=80), nullable=False),
        sa.PrimaryKeyConstraint("brand_id"),
    )
    op.create_table(
        "Models",
        sa.Column("model_id", sa.Integer(), nullable=False),
        sa.Column("model", sa.String(length=120), nullable=False),
        sa.Column("brand_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["brand_id"],
            ["Brands.brand_id"],
        ),
        sa.PrimaryKeyConstraint("model_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("Models")
    op.drop_table("Brands")
    # ### end Alembic commands ###
