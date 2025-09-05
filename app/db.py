import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from dotenv import load_dotenv
from contextlib import contextmanager

# Загружаем .env только если не production
if os.getenv("ENV") != "production":
    load_dotenv()

# Берём URL из окружения
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Please check .env or environment variables.")

# Создаём движок
engine = create_engine(DATABASE_URL)

# Настраиваем сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Удобный контекстный менеджер для работы с сессией
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Функция для инициализации БД (локально / для тестов)
def init_db():
    Base.metadata.create_all(bind=engine)