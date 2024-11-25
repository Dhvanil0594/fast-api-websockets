from pydantic import BaseModel

class GroupCreate(BaseModel):
    name: str
    is_private: bool

class GroupResponse(BaseModel):
    id: int
    name: str
    is_private: bool
