#!/usr/bin/with-contenv bash

# Запуск приложения
python /app/app/main.py --port=${FLASK_PORT:-5000}
