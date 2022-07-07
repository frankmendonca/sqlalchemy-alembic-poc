"""empty message

Revision ID: 6875d624d22a
Revises: 6c6fff279b9e
Create Date: 2022-07-07 14:20:46.767122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6875d624d22a"
down_revision = "6c6fff279b9e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("title", sa.String(length=50), nullable=False),
        sa.Column("content", sa.String(length=500), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("owner", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["owner"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("posts")
    # ### end Alembic commands ###
