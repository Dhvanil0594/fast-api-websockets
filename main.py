from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from src.routes.router import router

app = FastAPI()

# Include authentication routes
app.include_router(router)
