from sqlalchemy.orm import Session
from src.api.v1.models.message_models.message import Message
# from src.api.v1.schemas.message_schemas import MessageCreate

async def create_message(db: Session, db_message: Message):
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Message).offset(skip).limit(limit).all()
