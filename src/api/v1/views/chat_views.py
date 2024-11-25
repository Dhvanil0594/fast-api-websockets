from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from src.api.v1.repositories.group_membership_repository import add_user_to_group, get_group_members
from src.api.v1.repositories.group_repository import get_group_by_name
from src.api.v1.services.chat_service import chat_manager
from src.api.v1.schemas.message_schemas import MessageCreate, MessageResponse
from src.api.v1.repositories.message_repository import create_message, get_messages
from src.api.v1.repositories.user_repository import get_user_by_username
from src.api.v1.models.user_models.user import User
from src.api.v1.models.message_models.message import Message
from fastapi import Depends
from sqlalchemy.orm import Session
from database.database import get_db
router = APIRouter()

# WebSocket route
@router.websocket("/ws/group/{group_name}/{username}")
async def websocket_group_endpoint(websocket: WebSocket, group_name: str, username: str, db: Session = Depends(get_db)):
    # Accept the WebSocket connection first
    await websocket.accept()

    try:
        # Validate user and group
        user = await get_user_by_username(db, username)
        group = await get_group_by_name(db, group_name)
        if not user or not group:
            await websocket.send_text("Invalid user or group!")
            await websocket.close()
            return

        # Get current members of the group
        group_members_list = await get_group_members(db, group.id)

        # Check if the group is private and already has 2 members
        if group.is_private and len(group_members_list) >= 2:
            if not any(m.user_id == user.id for m in group_members_list):
                await websocket.send_text("This is a private group and is already full.")
                await websocket.close()
                return

        # Add user to the group if not already a member
        if not any(m.user_id == user.id for m in group_members_list):
            await add_user_to_group(db, user_id=user.id, group_id=group.id)

        # Connect WebSocket to the ChatManager for the specific group
        await chat_manager.connect(websocket, group_id=group.id)

        # Broadcast that the user has joined the group
        await chat_manager.broadcast(f"{username} joined {group_name}.", group_id=group.id)

        while True:
            # Receive message from the WebSocket
            data = await websocket.receive_text()

            # Broadcast message to the group members
            await chat_manager.broadcast(f"{username}: {data}", group_id=group.id)
            # await chat_manager.broadcast(f"{username} in {group_name}: {data}", group_id=group.id)

            # Save the message to the database
            # await create_message(db, Message(content=data, user_id=user.id))
            new_message = Message(content=data, user_id=user.id, group_id=group.id)
            await create_message(db, new_message)

    except WebSocketDisconnect:
        # Handle WebSocket disconnection
        await chat_manager.disconnect(websocket, group_id=group.id)
        await chat_manager.broadcast(f"{username} left {group_name}.", group_id=group.id)


# REST API for messages
# @router.post("/messages/", response_model=MessageResponse)
# async def send_message(message: MessageCreate, db: Session = Depends(get_db)):
#     message = Message(content=message.content, user_id=message.user_id, group_id=message.group_id)
#     db_message = await create_message(db, message)
#     return db_message

@router.get("/messages/", response_model=list[MessageResponse])
async def get_all_messages(db: Session = Depends(get_db), skip: int = 0, limit: int = 100, user_id: int = None, group_id: int = None):
    messages = await get_messages(db, skip=skip, limit=limit, user_id=user_id, group_id=group_id)
    for message in messages:
        message.group_name = message.group.name
        message.username = message.user.username
    return messages