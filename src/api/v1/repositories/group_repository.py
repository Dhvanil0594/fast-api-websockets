from sqlalchemy.orm import Session
from src.api.v1.models.group_models.group import Group
from src.api.v1.models.group_models.group_membership import GroupMembership
import sqlalchemy as sa


async def create_group(db: Session, name: str, is_private: bool):
    group = Group(name=name, is_private=is_private)
    db.add(group)
    db.commit()
    db.refresh(group)
    return group

async def get_group_by_name(db: Session, name: str):
    return db.query(Group).filter(Group.name == name).first()

async def get_all_groups(db: Session):
    return db.query(Group).all()

async def get_private_group_between_users(db: Session, user1_id: int, user2_id: int):
    # db.query(Group).filter(Group.is_private == True, GroupMembership.user_id.in_([user1_id, user2_id])).group_by(Group.id).having(sa.func.count(GroupMembership.user_id) == 2).first()
    # return (
    #     db.query(Group)
    #     .join(GroupMembership, Group.id == GroupMembership.group_id)
    #     .filter(
    #         Group.is_private == True,  # Check for private group
    #         GroupMembership.user_id.in_([user1_id, user2_id])  # Both users must be members
    #     )
    #     .group_by(Group.id)  # Ensure a single group is selected
    #     .having(sa.func.count(GroupMembership.user_id) == 2)  # Check for exactly 2 members
    #     .first()
    # )
    return (
        db.query(Group).filter(Group.is_private == True, GroupMembership.user_id.in_([user1_id, user2_id])).group_by(Group.id).having(sa.func.count(GroupMembership.user_id) == 2).first()
    )

