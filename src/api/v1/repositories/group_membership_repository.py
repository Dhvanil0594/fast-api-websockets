from sqlalchemy.orm import Session
from src.api.v1.models.group_models.group_membership import GroupMembership

async def add_user_to_group(db: Session, user_id: int, group_id: int):
    membership = GroupMembership(user_id=user_id, group_id=group_id)
    db.add(membership)
    db.commit()
    db.refresh(membership)
    return membership

async def get_group_members(db: Session, group_id: int):
    return db.query(GroupMembership).filter(GroupMembership.group_id == group_id).all()
