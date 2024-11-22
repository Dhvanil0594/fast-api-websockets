from pydantic import BaseModel, EmailStr
from typing import Optional

class MessageCreate(BaseModel):
    content: str
    user_id: int

class MessageResponse(BaseModel):
    id: int
    content: str
    user_id: int

