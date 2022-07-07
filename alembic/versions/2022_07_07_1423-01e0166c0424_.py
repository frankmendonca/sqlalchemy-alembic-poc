"""empty message

Revision ID: 01e0166c0424
Revises: 6875d624d22a
Create Date: 2022-07-07 14:23:37.832867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "01e0166c0424"
down_revision = "6875d624d22a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "posts", "owner", existing_type=sa.INTEGER(), nullable=False
    )
    op.create_index(op.f("ix_posts_owner"), "posts", ["owner"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_posts_owner"), table_name="posts")
    op.alter_column("posts", "owner", existing_type=sa.INTEGER(), nullable=True)
    # ### end Alembic commands ###