from contextlib import contextmanager
from database.database import SessionLocal

@contextmanager
def SqlAlchemyUnitOfWork():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise Exception(str(e))
    finally:
        db.close()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()