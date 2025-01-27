from contextlib import contextmanager
from sqlmodel import Session, create_engine
from sqlalchemy.sql import text
from app.core.config import (
    POSTGRES_USER,
    POSTGRES_SERVER,
    POSTGRES_DATABASE,
    POSTGRES_PASSWORD,
)

DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DATABASE}"

engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=5,
    pool_timeout=30,
    pool_recycle=1800,
)


@contextmanager
def get_db_session(schema_name: str):

    db = Session(autocommit=False, autoflush=False, bind=engine)
    try:
        db.execute(text(f"SET search_path TO {schema_name}"))
        yield db
    except Exception as e:
        print(f"Error connecting to the database with schema '{schema_name}': {e}")
        raise
    finally:
        db.close()
