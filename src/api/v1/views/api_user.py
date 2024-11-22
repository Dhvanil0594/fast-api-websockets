from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.api.v1.schemas.user_schemas import UserCreate, UserResponse
from src.api.v1.models.user_models.user import User
from src.api.v1.repositories.user_repository import create_user, get_user_by_email, get_user_by_id
from src.api.v1.services.auth_service import hash_password
from database.database import get_db
from logger import logger

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    
    if not user.username or not user.email or not user.password:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="username, email, and password are required")

    # Check if the email is already registered
    if (await get_user_by_email(db, user.email)) is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    try:
        hashed_password = hash_password(user.password)
        db_user = User(username=user.username, email=user.email, password=hashed_password)
        db_user = await create_user(db, db_user)
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating user")

    return db_user

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = await get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
