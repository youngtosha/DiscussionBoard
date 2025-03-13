import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env-файла (если он есть)
load_dotenv()

# Конфигурация базы данных
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")
"""str: URL подключения к базе данных. По умолчанию используется SQLite."""

# Секретный ключ для JWT-токенов и других криптографических операций
SECRET_KEY = os.getenv("SECRET_KEY", "random_secret_key")
"""str: Секретный ключ для подписи токенов. Используется в аутентификации."""

# Алгоритм хеширования паролей и подписи токенов
ALGORITHM = os.getenv("ALGORITHM", "HS256")
"""str: Алгоритм хеширования, используемый для генерации JWT."""

# Время жизни токена (в минутах)
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
"""int: Время жизни токена доступа в минутах."""

# Настройка режима разработки (например, для логирования)
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() in ["true", "1"]
"""bool: Флаг режима отладки (True/False)."""

# Указываем поддержку нескольких типов БД (если нужно)
SUPPORTED_DATABASES = ["sqlite", "postgresql", "mysql"]
"""list: Поддерживаемые типы баз данных."""

# Проверяем, что выбранная база данных поддерживается
if not any(db in DATABASE_URL for db in SUPPORTED_DATABASES):
    raise ValueError(f"Неподдерживаемый тип базы данных в {DATABASE_URL}")
