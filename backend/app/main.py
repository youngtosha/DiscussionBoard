from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth

# Создание FastAPI-приложения
app = FastAPI(
    title="Discussion Board API",
    description="API для форума с поддержкой ролей пользователей (гость, посетитель, модератор, администратор).",
    version="1.0.0",
    contact={
        "name": "Support Team",
        "email": "support@example.com",
    },
)

# Настройки CORS (если клиентское приложение работает на другом домене)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает запросы с любых источников (в продакшене лучше ограничить)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешены все методы (GET, POST, PUT, DELETE и т. д.)
    allow_headers=["*"],  # Разрешены все заголовки
)

# Подключение роутеров
app.include_router(auth.router, prefix="/auth")

@app.get("/", tags=["Root"])
async def root():
    """
    Приветственное сообщение API.

    **Возвращает:**
    - `dict`: JSON-ответ с приветствием.
    """
    return {"message": "Welcome to the Discussion Board API"}
