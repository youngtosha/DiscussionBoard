import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
