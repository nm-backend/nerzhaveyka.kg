FROM python:3.13-slim

# Отключаем буферизацию Python и создание .pyc файлов
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Обновляем pip и устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# Копируем приложение
COPY . .

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Открываем порт
EXPOSE 8000

# Запускаем приложение через Gunicorn
CMD ["gunicorn", "nerzhaveyka.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "60"]
