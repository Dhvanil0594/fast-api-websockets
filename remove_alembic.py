from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from config.config import settings


MASTER_DB_URL = f"postgresql+psycopg2://{settings.MASTER_DB_USER}:{settings.MASTER_DB_PASSWORD}@{settings.MASTER_DB_HOSTNAME}:{settings.MASTER_DB_PORT}/{settings.MASTER_DB_NAME}"
table_name_to_delete = "alembic_version"


def delete_table_from_database():
    # Create a SQLAlchemy engine
    engine = create_engine(MASTER_DB_URL)
    Base = declarative_base()

    # Create a metadata object
    metadata = MetaData()
    metadata.create_all(engine, checkfirst=True)
    # Reflect the existing database schema
    metadata.reflect(bind=engine)

    # Get the table to delete
    table = metadata.tables[table_name_to_delete]

    # Drop the table
    if table is not None:
        Base.metadata.drop_all(engine, [table], checkfirst=True)


if __name__ == "__main__":
    delete_table_from_database()
