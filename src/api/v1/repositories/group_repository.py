from sqlalchemy.orm import Session
from src.api.v1.models.group_models.group import Group

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
