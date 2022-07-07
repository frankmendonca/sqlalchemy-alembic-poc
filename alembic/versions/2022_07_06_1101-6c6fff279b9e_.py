"""empty message

Revision ID: 6c6fff279b9e
Revises: 912b2eabf029
Create Date: 2022-07-06 14:11:22.613894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6c6fff279b9e"
down_revision = "912b2eabf029"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "users", ["username"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("users_username_key", "users", type_="unique")
    # ### end Alembic commands ###
