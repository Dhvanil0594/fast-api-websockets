from sqlalchemy.orm import Session
from src.api.v1.models.user_models.user import User
# from src.api.v1.schemas.user_schemas import UserCreate

async def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

async def create_user(db: Session, db_user: User):
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

async def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

async def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()