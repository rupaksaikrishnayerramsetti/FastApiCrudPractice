"""Creating students table

Revision ID: 10bce61e70c1
Revises: 
Create Date: 2024-06-18 15:50:45.639640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10bce61e70c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("students", 
                    sa.Column("reg_id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
                    sa.Column("name", sa.String(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("branch", sa.String(), nullable=False),
                    sa.Column("section", sa.String(), nullable=False),
                    sa.Column("is_deleted", sa.Boolean(), default=False, nullable=True),
                    sa.PrimaryKeyConstraint("reg_id")
                    )


def downgrade() -> None:
    op.drop_table("students")
