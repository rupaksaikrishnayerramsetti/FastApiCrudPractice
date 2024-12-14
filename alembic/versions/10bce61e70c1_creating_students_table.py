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
    # op.create_table("datasets",
    #                 sa.Column("id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
    #                 sa.Column("name", sa.String(), nullable=False),
    #                 sa.Column("description", sa.String()),
    #                 sa.Column("file_path", sa.String()),
    #                 sa.Column("storage_path", sa.String()),
    #                 sa.Column("size", sa.Integer()),
    #                 sa.Column("number_of_files", sa.Integer()),
    #                 sa.Column("creation_date", sa.DateTime(), nullable=False),
    #                 sa.Column("last_modified_date", sa.DateTime(), nullable=False),
    #                 sa.Column("status", sa.String()),
    #                 sa.Column("tags", sa.ARRAY(sa.String())),
    #                 sa.Column("owner_id", sa.String()),
    #                 sa.Column("owner_name", sa.String()),
    #                 sa.Column("created_by_id", sa.String()),
    #                 sa.Column("created_by_name", sa.String()),
    #                 sa.Column("last_modified_by_id", sa.String()),
    #                 sa.Column("last_modified_by_name", sa.String()),
    #                 sa.Column("sql", sa.String()),
    #                 sa.Column("workflow_id", sa.String())
    #                 )


def downgrade() -> None:
    op.drop_table("students")
