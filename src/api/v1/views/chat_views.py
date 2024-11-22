from fastapi import APIRouter, WebSocket, WebSocketDisconnect
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
@router.websocket("/ws/chat/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str, db: Session = Depends(get_db)):
    await chat_manager.connect(websocket)
    try:
        # Find the user from the database
        user = await get_user_by_username(db, username)
        if user is None:
            await websocket.send_text("User not found!")
            await websocket.close()
            return

        while True:
            data = await websocket.receive_text()  # Receive message
            # Broadcast the message to other users
            await chat_manager.broadcast(f"{username}: {data}")

            # Save the message in the database
            await create_message(db, Message(content=data, user_id=user.id))
    except WebSocketDisconnect:
        await chat_manager.disconnect(websocket)
        await chat_manager.broadcast(f"{username} left the chat")

# REST API for messages
@router.post("/messages/", response_model=MessageResponse)
def send_message(message: MessageCreate, db: Session = Depends(get_db)):
    message = Message(content=message.content, user_id=message.user_id)
    db_message = create_message(db, message)
    return db_message

@router.get("/messages/", response_model=list[MessageResponse])
def get_all_messages(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    messages = get_messages(db, skip=skip, limit=limit)
    return messages