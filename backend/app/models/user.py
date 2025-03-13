from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    """
    Модель пользователя для базы данных.

    Атрибуты:
        id (int): Уникальный идентификатор пользователя.
        username (str): Уникальное имя пользователя.
        email (str): Уникальный email пользователя.
        password_hash (str): Хеш пароля пользователя.
        role (str): Роль пользователя (по умолчанию "visitor").
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="visitor")  # guest, visitor, moderator, admin

    def __repr__(self):
        """Возвращает строковое представление объекта User."""
        return f"<User(id={self.id}, username={self.username}, email={self.email}, role={self.role})>"

    def set_password(self, password: str):
        """
        Устанавливает хеш пароля для пользователя.

        :param password: Строка с паролем пользователя.
        """
        from hashlib import sha256
        self.password_hash = sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        """
        Проверяет, совпадает ли переданный пароль с сохраненным хешем.

        :param password: Строка с паролем для проверки.
        :return: True, если пароли совпадают, иначе False.
        """
        from hashlib import sha256
        return self.password_hash == sha256(password.encode()).hexdigest()

    def is_admin(self) -> bool:
        """
        Проверяет, является ли пользователь администратором.

        :return: True, если роль пользователя - "admin".
        """
        return self.role == "admin"

    def to_dict(self) -> dict:
        """
        Преобразует объект пользователя в словарь.

        :return: Словарь с данными пользователя (без пароля).
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role
        }