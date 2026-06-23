#!/bin/bash

# entrypoint.sh - точка входа для Docker контейнера

echo "Применяем миграции..."
python manage.py migrate

echo "Собираем статические файлы..."
python manage.py collectstatic --noinput

echo "Запускаем Gunicorn..."
exec gunicorn nerzhaveyka.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --worker-class sync \
    --timeout 60 \
    --access-logfile - \
    --error-logfile - \
    "$@"
