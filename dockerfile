FROM python:3.12

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование вашего кода
COPY . /app

WORKDIR /app

# Запуск приложения
CMD ["python", "app.py"]
