import uvicorn
from alembic.config import Config
from alembic import command
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from config.config import settings

MASTER_DB_URL = f"postgresql+psycopg2://{settings.MASTER_DB_USER}:{settings.MASTER_DB_PASSWORD}@{settings.MASTER_DB_HOSTNAME}:{settings.MASTER_DB_PORT}/{settings.MASTER_DB_NAME}"


def run_migrations():
  try:
    engine = create_engine(MASTER_DB_URL)
    Base = declarative_base()

    # Create a metadata object
    metadata = MetaData()
    metadata.create_all(bind=engine, checkfirst=True)

    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", MASTER_DB_URL)
    print(f"Running Alembic migrations on database: {MASTER_DB_URL}")
    command.upgrade(alembic_cfg, "head")
    print("Alembic migrations completed successfully.")
  except Exception as e:
    print(f"Error running migrations: {e}")


if __name__ == "__main__":
  # Run migrations before starting the app
  run_migrations()

  uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=settings.DEBUG)

'''
openssl rand -hex 32 used for generating secret key
'''
