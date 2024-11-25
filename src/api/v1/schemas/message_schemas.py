from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class MessageCreate(BaseModel):
    content: str
    user_id: int
    group_id: int

class MessageResponse(BaseModel):
    id: int
    content: str
    user_id: int
    username: str
    group_id: int
    group_name: str
    created_at: datetime
