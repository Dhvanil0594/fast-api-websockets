from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database.database import Base

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    is_private = Column(Boolean, default=False)  # Now using Boolean for private/public

    members = relationship("GroupMembership", back_populates="group")
