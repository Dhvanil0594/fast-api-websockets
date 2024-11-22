from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import settings

# MASTER_DB_URL = f"mysql://{settings.MASTER_DB_USER}:{settings.MASTER_DB_PASSWORD}@{settings.MASTER_DB_HOSTNAME}:{settings.MASTER_DB_PORT}/{settings.MASTER_DB_NAME}"
MASTER_DB_URL = f"postgresql+psycopg2://{settings.MASTER_DB_USER}:{settings.MASTER_DB_PASSWORD}@{settings.MASTER_DB_HOSTNAME}:{settings.MASTER_DB_PORT}/{settings.MASTER_DB_NAME}"
engine = create_engine(MASTER_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
