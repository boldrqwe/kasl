FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости (если есть)
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем точку входа
CMD ["python", "run_container.py"]
