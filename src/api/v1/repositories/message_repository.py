from sqlalchemy.orm import Session
from src.api.v1.models.message_models.message import Message
# from src.api.v1.schemas.message_schemas import MessageCreate

async def create_message(db: Session, db_message: Message):
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

async def get_messages(db: Session, skip: int = 0, limit: int = 100, user_id: int = None, group_id: int = None):
    # return db.query(Message).offset(skip).limit(limit).all()
    query = db.query(Message)
    if user_id:
        query = query.filter(Message.user_id == user_id)
    if group_id:
        query = query.filter(Message.group_id == group_id)
    return query.offset(skip).limit(limit).all()
