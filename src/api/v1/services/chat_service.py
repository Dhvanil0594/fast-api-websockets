# from fastapi import WebSocket, WebSocketDisconnect
# from typing import List

# class ChatManager:
#     def __init__(self):
#         self.active_connections: List[WebSocket] = []

#     async def connect(self, websocket: WebSocket):
#         await websocket.accept()
#         self.active_connections.append(websocket)

#     async def disconnect(self, websocket: WebSocket):
#         self.active_connections.remove(websocket)

#     async def send_personal_message(self, message: str, websocket: WebSocket):
#         await websocket.send_text(message)

#     async def broadcast(self, message: str):
#         for connection in self.active_connections:
#             await connection.send_text(message)

# chat_manager = ChatManager()

# # =========================================== Working ====================================================================

# from fastapi import WebSocket, WebSocketDisconnect

# class ChatManager:
#     def __init__(self):
#         # Store connections grouped by group_id
#         self.active_connections: dict[int, list[WebSocket]] = {}

#     async def connect(self, websocket: WebSocket, group_id: int):
#         """Accept a new WebSocket connection and add it to the group."""
#         await websocket.accept()
#         if group_id not in self.active_connections:
#             self.active_connections[group_id] = []
#         self.active_connections[group_id].append(websocket)

#     async def disconnect(self, websocket: WebSocket, group_id: int):
#         """Remove a WebSocket connection from the group."""
#         if group_id in self.active_connections:
#             self.active_connections[group_id].remove(websocket)
#             if not self.active_connections[group_id]:  # Clean up if empty
#                 del self.active_connections[group_id]

#     async def send_personal_message(self, message: str, websocket: WebSocket):
#         """Send a personal message to a specific WebSocket connection."""
#         await websocket.send_text(message)

#     async def broadcast(self, message: str, group_id: int):
#         """Broadcast a message to all members of the specified group."""
#         if group_id in self.active_connections:
#             for connection in self.active_connections[group_id]:
#                 await connection.send_text(message)

#     def get_connection_by_user_id(self, group_id: int, user_id: int, user_socket_map: dict[int, WebSocket]):
#         """
#         Retrieve the WebSocket connection for a specific user in a group.
#         `user_socket_map` should provide a mapping of user_id -> WebSocket.
#         """
#         if group_id in self.active_connections:
#             return user_socket_map.get(user_id, None)  # Get WebSocket if user exists

# # Create a shared instance of ChatManager
# chat_manager = ChatManager()

# # ==================================================================================================================
from fastapi import WebSocket, WebSocketDisconnect
class ChatManager:
    def __init__(self):
        self.active_connections: dict[int, list[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, group_id: int):
        """Add a WebSocket connection to a specific group."""
        if group_id not in self.active_connections:
            self.active_connections[group_id] = []
        self.active_connections[group_id].append(websocket)

    async def disconnect(self, websocket: WebSocket, group_id: int):
        """Remove a WebSocket connection from a specific group."""
        if group_id in self.active_connections:
            self.active_connections[group_id].remove(websocket)
            if not self.active_connections[group_id]:
                del self.active_connections[group_id]

    async def broadcast(self, message: str, group_id: int):
        """Broadcast a message to all active connections in a specific group."""
        if group_id in self.active_connections:
            for connection in self.active_connections[group_id]:
                await connection.send_text(message)

chat_manager = ChatManager()