import uvicorn
from alembic.config import Config
from alembic import command
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from config.config import settings

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=settings.DEBUG)