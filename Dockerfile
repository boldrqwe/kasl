# Dockerfile
FROM docker/compose:latest

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл docker-compose.yml
COPY docker-compose.yml .

# Запуск docker-compose
CMD ["docker-compose", "up"]
