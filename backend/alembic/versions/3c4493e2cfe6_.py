"""
Revision ID: 3c4493e2cfe6
Revises: bcf6c57b9aa7
Create Date: 2026-03-29 16:01:06.894216
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '3c4493e2cfe6'
down_revision: Union[str, Sequence[str], None] = 'bcf6c57b9aa7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("character_episode")

    op.create_table(
        "character_episode",
        sa.Column(
            "character_id",
            sa.Integer(),
            sa.ForeignKey("characters.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column(
            "episode_id",
            sa.Integer(),
            sa.ForeignKey("episodes.id", ondelete="CASCADE"),
            primary_key=True,
        ),
    )

    with op.batch_alter_table("characters") as batch_op:
        batch_op.add_column(sa.Column("external_id", sa.Integer(), nullable=False))
        batch_op.create_unique_constraint(
            "uq_characters_external_id",
            ["external_id"],
        )

    with op.batch_alter_table("episodes") as batch_op:
        batch_op.add_column(sa.Column("external_id", sa.Integer(), nullable=False))
        batch_op.create_unique_constraint(
            "uq_episodes_external_id",
            ["external_id"],
        )

    with op.batch_alter_table("locations") as batch_op:
        batch_op.add_column(sa.Column("external_id", sa.Integer(), nullable=False))
        batch_op.create_unique_constraint(
            "uq_locations_external_id",
            ["external_id"],
        )


def downgrade() -> None:
    with op.batch_alter_table("locations") as batch_op:
        batch_op.drop_constraint("uq_locations_external_id", type_="unique")
        batch_op.drop_column("external_id")

    with op.batch_alter_table("episodes") as batch_op:
        batch_op.drop_constraint("uq_episodes_external_id", type_="unique")
        batch_op.drop_column("external_id")

    with op.batch_alter_table("characters") as batch_op:
        batch_op.drop_constraint("uq_characters_external_id", type_="unique")
        batch_op.drop_column("external_id")

    op.drop_table("character_episode")

    op.create_table(
        "character_episode",
        sa.Column("character_id", sa.Integer(), sa.ForeignKey("characters.id"), primary_key=True),
        sa.Column("episode_id", sa.Integer(), sa.ForeignKey("episodes.id"), primary_key=True),
    )