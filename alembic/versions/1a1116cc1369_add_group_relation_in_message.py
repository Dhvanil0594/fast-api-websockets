"""add group relation in message.

Revision ID: 1a1116cc1369
Revises: be8164cdd5c7
Create Date: 2024-11-25 11:49:20.105686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1a1116cc1369'
down_revision: Union[str, None] = 'be8164cdd5c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # Step 1: Add the group_id column as nullable first
    op.add_column('messages', sa.Column('group_id', sa.Integer(), nullable=True))
    
    # Step 2: Add foreign key constraint (this can be deferred until after nullability is allowed)
    op.create_foreign_key('fk_messages_group_id', 'messages', 'groups', ['group_id'], ['id'], ondelete="CASCADE")
    
    # Step 3: Now that the group_id column is in place and nullable, update the existing rows (optional)
    # If you have a default group_id, set it for all existing messages
    op.execute('UPDATE messages SET group_id = 1 WHERE group_id IS NULL')  # Example, using 1 as the default group_id
    
    # Step 4: Alter the column to be NOT NULL after existing rows have been populated
    op.alter_column('messages', 'group_id', nullable=False)
    
    # Step 5: If you need to enforce other constraints (content, user_id, created_at), ensure they are NOT NULL
    op.alter_column('messages', 'content', nullable=False)
    op.alter_column('messages', 'user_id', nullable=False)
    op.alter_column('messages', 'created_at', nullable=False)


def downgrade():
    # Reverse the migration
    op.drop_constraint('fk_messages_group_id', 'messages', type_='foreignkey')
    op.drop_column('messages', 'group_id')
    op.alter_column('messages', 'created_at', nullable=True)
    op.alter_column('messages', 'user_id', nullable=True)
    op.alter_column('messages', 'content', nullable=True)