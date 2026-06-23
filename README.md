# Нержавейка — Веб-сайт компании


Веб-сайт компании "Нержавейка Борбору" — производство и продажа изделий из нержавеющей стали в городе Ош, Кыргызстан.

## 📋 Описание

Сайт представляет собой современный, адаптивный веб-сайт с информацией о компании, каталогом продуктов, галереей работ и формой обратной связи.

**Основные разделы:**
- Главная страница с информацией о компании
- О компании
- Каталог продуктов и услуг
- Галерея выполненных работ
- Страница контактов
- Интеграция с картами и социальными сетями

## 🛠️ Технологический стек

- **Backend:** Django 5.0.6
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Database:** SQLite (разработка), PostgreSQL (продакшен - рекомендуется)
- **Server:** Gunicorn + Nginx (продакшен)
- **Package Manager:** pip

## 📦 Требования

- Python 3.10+
- pip (Python Package Installer)
- Git

## 🚀 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/nerzhaveyka.git
cd nerzhaveyka
```

### 2. Создание виртуального окружения

```bash
python -m venv venv

# На Windows:
venv\Scripts\activate

# На Linux/macOS:
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

```bash
# Скопируйте файл примера
cp .env.example .env

# Отредактируйте .env с вашими значениями
# Важно: Сгенерируйте новый SECRET_KEY для продакшена
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 5. Запуск миграций

```bash
python manage.py migrate
```

### 6. Создание суперпользователя (администратора)

```bash
python manage.py createsuperuser
```

### 7. Сбор статических файлов

```bash
python manage.py collectstatic --noinput
```

### 8. Запуск сервера разработки

```bash
python manage.py runserver
```

Теперь сайт доступен по адресу: http://127.0.0.1:8000/

## 📁 Структура проекта

```
nerzhaveyka/
├── core/                      # Основное приложение Django
│   ├── migrations/           # Миграции БД
│   ├── models.py            # Модели данных (в разработке)
│   ├── views.py             # Представления
│   ├── urls.py              # URL маршруты
│   └── admin.py             # Конфигурация админ-панели
│
├── nerzhaveyka/              # Конфигурация проекта Django
│   ├── settings.py          # Основные настройки
│   ├── urls.py              # Главные URL маршруты
│   ├── wsgi.py              # WSGI приложение
│   └── __init__.py
│
├── templates/                # HTML шаблоны
│   ├── base.html            # Базовый шаблон
│   ├── index.html           # Главная страница
│   ├── about.html           # О компании
│   ├── products.html        # Каталог продуктов
│   ├── gallery.html         # Галерея работ
│   ├── contacts.html        # Контакты
│   └── headfoot/            # Компоненты
│       ├── header.html      # Шапка сайта
│       ├── footer.html      # Подвал сайта
│       ├── cta.html         # CTA форма
│       └── placeholder.html # Заглушка изображений
│
├── static/                   # Статические файлы
│   ├── css/
│   │   └── style.css        # Основные стили
│   ├── js/
│   │   └── main.js          # JavaScript функциональность
│   └── img/                 # Изображения
│
├── media/                    # Загруженные пользователями файлы
├── manage.py                # Django управление
├── requirements.txt         # Зависимости проекта
├── .env.example            # Пример переменных окружения
└── README.md               # Этот файл
```

## 🔧 Конфигурация

### Переменные окружения (.env)

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost 127.0.0.1 nerzhaveyka.kg
LANGUAGE_CODE=ru-ru
TIME_ZONE=Asia/Bishkek
```

### Поддерживаемые языки
- Русский (ru-ru)

### Часовой пояс
- Asia/Bishkek (Кыргызстан)

## 📱 Адаптивность

Сайт полностью адаптирован для всех устройств:
- **Десктопы:** 1920px и более
- **Планшеты:** 768px - 1919px
- **Мобильные:** до 767px

## 🎨 Дизайн

- **Цветовая схема:** Темная палитра с синим акцентом
- **Шрифт:** Manrope (с резервными системными шрифтами)
- **Радиусы скругления:** 8px, 14px, 22px, 999px
- **Адаптивный дизайн:** CSS Grid, Flexbox

## ⚙️ Администрирование

Перейдите в админ-панель: http://127.0.0.1:8000/admin/

Используйте учетные данные суперпользователя, которые вы создали.

## 🚀 Развертывание

### Быстрый старт с Docker (Рекомендуется)

```bash
# Используйте скрипт быстрого запуска
chmod +x start-docker.sh
./start-docker.sh
```

Или вручную:
```bash
# Запустите контейнеры
docker-compose up --build -d

# Создайте суперпользователя
docker-compose exec web python manage.py createsuperuser

# Проверьте URL
# - Сайт: http://localhost:8000
# - Админ: http://localhost:8000/admin
# - API: http://localhost:8000/api
# - API Docs: http://localhost:8000/api/docs
```

### Продакшен - Подробное руководство

Смотрите [DEPLOYMENT.md](DEPLOYMENT.md) для полного руководства по развертыванию на продакшене, включая:
- Настройку SSL с Let's Encrypt
- Конфигурацию Nginx
- Автоматическое обновление сертификатов
- Резервные копии БД
- Решение проблем

### Локальная разработка без Docker

```bash
# 1. Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # или на Windows: venv\Scripts\activate

# 2. Установите зависимости
pip install -r requirements.txt

# 3. Примените миграции
python manage.py migrate

# 4. Создайте суперпользователя
python manage.py createsuperuser

# 5. Запустите сервер разработки
python manage.py runserver
```

## 📊 Производительность

- Минификация CSS и JavaScript
- Оптимизация изображений
- Кеширование браузера
- CDN для статических файлов (рекомендуется)

## 🔒 Безопасность

- ✅ CSRF защита на всех формах
- ✅ XSS защита
- ✅ SQL инъекции защита (через ORM)
- ⚠️ Убедитесь, что установлена переменная `SECRET_KEY` для продакшена
- ⚠️ Установите `DEBUG=False` для продакшена
- ⚠️ Используйте HTTPS в продакшене

## 📝 TODO

- [ ] Создать модели для Product, GalleryImage, ContactSubmission
- [ ] Реализовать обработку формы контактов
- [ ] Добавить API endpoints
- [ ] Интегрировать с системой платежей
- [ ] Добавить систему уведомлений по email
- [ ] Реализовать поиск по продуктам
- [ ] Добавить фильтры в каталог
- [ ] Реализовать систему отзывов
- [ ] Добавить интеграцию с WhatsApp
- [ ] Добавить многоязычность

## 📞 Контакты

**Компания:** Нержавейка Борбору  
**Город:** Ош, Кыргызстан  
**Телефон:** +996 998 666 555 / +996 778 666 555  
**Email:** info@nerzhaveyka.kg  
**Адрес:** HQ5C+RF4, Ош

## 🤝 Вклад

Если вы хотите внести свой вклад в проект:

1. Сделайте Fork репозитория
2. Создайте ветку для вашей фичи (`git checkout -b feature/AmazingFeature`)
3. Commitьте ваши изменения (`git commit -m 'Add some AmazingFeature'`)
4. Pushьте в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект лицензирован под MIT License - смотрите файл [LICENSE](LICENSE) для деталей.

## 🙏 Благодарности

- Спасибо команде Django за отличный фреймворк
- Спасибо дизайнеру за красивый макет
- Спасибо всем, кто внес вклад в проект

---

**Последнее обновление:** 2024-06-19  
**Версия:** 1.0.0  
**Статус:** В разработке ⚠️
# nerzhaveyka.kg
https://nerzhaveyka.kg/ clone
