* * * * *

Chat Application with FastAPI and WebSockets
============================================

This project is a simple chat application built with **FastAPI** and **WebSockets**. It allows users to connect to a real-time chat, send and receive messages, and save messages in a database.

Features
--------

-   Real-time communication via WebSockets.
-   User authentication (simple username-based).
-   Messages are stored in a database (SQLAlchemy with Postgresql).
-   Broadcast messages to all connected users.
-   Store and retrieve chat messages.

Technologies Used
-----------------

-   **Backend**: FastAPI
-   **WebSockets**: For real-time messaging.
-   **Database**: Postgresql, SQLAlchemy ORM
-   **ORM**: SQLAlchemy
-   **Authentication**: Simple username-based user system.

Installation
------------

### Prerequisites

1.  **Python** (3.10+)
2.  **Postgresql** (or any supported relational database)
3.  **FastAPI** and **Uvicorn** for running the app
4.  **SQLAlchemy** for database interactions

### Step-by-Step Installation

1.  **Clone the repository**:

    ```
    git clone https://github.com/Dhvanil0594/fast-api-websockets    
    cd chat-app
    ```

2.  **Create and activate a virtual environment**:

    ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:

    ```
    pip install -r requirements.txt
    ```

4.  **Set up your database**:

    -   Configure your Postgresql credentials in the .env file. For example:

        ```
        MASTER_DB_USER = "your_db_user"
        MASTER_DB_PASSWORD = "your_db_password"
        MASTER_DB_HOSTNAME = "localhost"
        MASTER_DB_PORT = "your_db_port"
        MASTER_DB_NAME = "chat_db"
        ```

5.  **Run the application**:

    ```
    python run.py
    ```

    This will start the server on `http://localhost:8000`.

WebSocket Endpoints
-------------------

### Connect to the WebSocket

The WebSocket route allows users to connect to the chat service and send/receive messages in real-time.

#### URL: `/ws/group/{group_name}/{username}`

-   **Parameters**:
    -   `group_name`: The name of the chat group.
    -   `username`: The unique identifier for each user.

#### Features:

-   Upon successful connection, the user will be able to send and receive messages in real-time.
-   If the user does not exist in the database, the WebSocket connection will be closed.
-   Messages are saved in the database and broadcasted to all connected users.

API Endpoints
-------------

### API Endpoints

The FastAPI application provides the following endpoints:

#### URL: `/api/v1/users/`

-   **Method**: `POST`

-   **Description**: Create a new user.

#### URL: `/api/users/{user_id}`

-   **Method**: `GET`

-   **Description**: Retrieve information about a specific user.

#### URL: `/api/v1/groups/`

-   **Method**: `POST`

-   **Description**: Create a new group. There are 2 types private and public. Private means only 2 users in that group and Public means any number of users.

#### URL: `/api/v1/groups/`

-   **Method**: `GET`

-   **Description**: Retrieve a list of all groups.

#### URL: `/api/v1/messages/`

-   **Method**: `GET`

-   **Query Params(optional)**: skip, limit, group_id, user_id

-   **Description**: Retrieve a list of all messages.

