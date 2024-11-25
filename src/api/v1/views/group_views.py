from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.api.v1.schemas.group_schemas import GroupCreate, GroupResponse
from src.api.v1.repositories.group_repository import create_group, get_all_groups
# from database.database import get_db
from database.unit_of_work import get_db

router = APIRouter()

@router.post("/groups/", response_model=GroupResponse)
async def create_new_group(group: GroupCreate, db: Session = Depends(get_db)):
    return await create_group(db, group.name, group.is_private)

@router.get("/groups/", response_model=list[GroupResponse])
async def get_groups(db: Session = Depends(get_db)):
    return await get_all_groups(db)
