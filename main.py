from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from src.routes.router import router
# from fastapi_project.database.database import engine, Base

# Create all tables from models
# Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include authentication routes
app.include_router(router)

# if __name__ == "__main__":
#     uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
