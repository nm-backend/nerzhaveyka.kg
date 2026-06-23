#!/bin/bash

# start-docker.sh - скрипт для быстрого запуска Docker контейнеров

set -e

echo "================================"
echo "Нержавейка - Docker Startup"
echo "================================"
echo ""

# Проверяем наличие .env файла
if [ ! -f ".env" ]; then
    echo "⚠️  Файл .env не найден. Копируем из .env.example..."
    cp .env.example .env
    echo "✅ Создан .env файл. Пожалуйста, отредактируйте его с вашими параметрами."
    echo ""
fi

# Проверяем Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker не установлен. Пожалуйста, установите Docker."
    exit 1
fi

# Проверяем Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose не установлен. Пожалуйста, установите Docker Compose."
    exit 1
fi

echo "🐳 Запускаем Docker контейнеры..."
docker-compose up --build -d

echo ""
echo "⏳ Ожидаем готовности базы данных..."
sleep 10

echo ""
echo "✅ Docker контейнеры запущены!"
echo ""
echo "📍 Доступные URL:"
echo "   - Веб-сайт: http://localhost:8000"
echo "   - Админ-панель: http://localhost:8000/admin"
echo "   - API: http://localhost:8000/api"
echo "   - API Docs: http://localhost:8000/api/docs"
echo "   - PostgreSQL: localhost:5432"
echo ""
echo "📝 Для просмотра логов:"
echo "   docker-compose logs -f web"
echo ""
echo "🛑 Для остановки контейнеров:"
echo "   docker-compose down"
echo ""
