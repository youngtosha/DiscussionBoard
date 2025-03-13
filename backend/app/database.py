from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL

# Проверяем, является ли база данных SQLite (для правильной настройки аргументов подключения)
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

# Создание движка SQLAlchemy для работы с базой данных
engine = create_engine(DATABASE_URL, connect_args=connect_args)
"""SQLAlchemy Engine: Управляет подключением к базе данных."""

# Создание локальной сессии для взаимодействия с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""sessionmaker: Фабрика для создания сессий работы с БД."""

# Базовый класс для всех моделей SQLAlchemy
Base = declarative_base()
"""DeclarativeMeta: Базовый класс для моделей ORM."""

def get_db():
    """
    Генератор зависимостей для получения сессии базы данных.

    **Использование в FastAPI:**
    ```python
    from fastapi import Depends
    from app.database import get_db

    @app.get("/items/")
    def read_items(db: Session = Depends(get_db)):
        return db.query(Item).all()
    ```

    **Возвращает:**
    - `Session`: Объект сессии SQLAlchemy.

    **Гарантирует:**
    - Автоматическое закрытие сессии после выполнения запроса.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
