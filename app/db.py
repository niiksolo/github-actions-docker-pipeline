import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from dotenv import load_dotenv
from contextlib import contextmanager


if os.getenv("ENV") != "production":
    load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Please check .env or environment variables.")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)