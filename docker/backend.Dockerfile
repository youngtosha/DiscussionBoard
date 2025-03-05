# Используем Python 3.11
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY backend/requirements.txt /app/requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY backend /app

# Запускаем сервер
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
