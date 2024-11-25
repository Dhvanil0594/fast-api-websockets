from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from src.routes.router import router
from fastapi.middleware.cors import CORSMiddleware
from config.endpoints_tags import tags_metadata
from config.config import settings

app = FastAPI(openapi_tags=tags_metadata, title="Chat Application")

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=("DELETE", "GET", "PATCH", "POST", "PUT"),
                   allow_headers=["*"])

# Include authentication routes
app.include_router(router)
