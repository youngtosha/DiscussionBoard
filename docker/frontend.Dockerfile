# Используем Node.js 18
FROM node:18

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы package.json и package-lock.json
COPY frontend/package.json frontend/package-lock.json /app/

# Устанавливаем зависимости
RUN npm install

# Копируем исходный код
COPY frontend /app

# Собираем проект
RUN npm run build

# Запускаем сервер
CMD ["npm", "start"]
