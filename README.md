# Нержавейка — сайт компании

Корпоративный сайт компании «Нержавейка Борбору» (Ош, Кырgyzstan): каталог, галерея, контакты, REST API.

**Стек:** Django 5, DRF, HTML/CSS/JS, SQLite или PostgreSQL, Gunicorn, Nginx, WhiteNoise.

## Локальный запуск

```bash
git clone https://github.com/nm-backend/nerzhaveyka.kg.git
cd nerzhaveyka.kg
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/macOS
pip install -r requirements.txt
copy .env.example .env         # Windows
# cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Сайт: http://127.0.0.1:8000/  
Админка: http://127.0.0.1:8000/admin/  
API docs: http://127.0.0.1:8000/api/swagger/

## Переменные окружения (.env)

| Переменная | Описание |
|------------|----------|
| `SECRET_KEY` | Секрет Django (обязателен на сервере) |
| `DEBUG` | `True` локально, `False` на сервере |
| `ALLOWED_HOSTS` | Домены через запятую |
| `CSRF_TRUSTED_ORIGINS` | `https://ваш-домен.kg` |
| `DATABASE_ENGINE` | `sqlite` или `postgresql` |

Сгенерировать ключ:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Деплой на VPS (Ubuntu)

### 1. Подготовка сервера

```bash
sudo apt update && sudo apt install -y python3-venv python3-pip nginx git
sudo mkdir -p /var/www/nerzhaveyka
sudo chown $USER:$USER /var/www/nerzhaveyka
git clone https://github.com/nm-backend/nerzhaveyka.kg.git /var/www/nerzhaveyka
cd /var/www/nerzhaveyka
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
nano .env
```

В `.env` на сервере: `DEBUG=False`, свой `SECRET_KEY`, домены в `ALLOWED_HOSTS` и `CSRF_TRUSTED_ORIGINS`.

### 2. База и статика

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
mkdir -p media
```

### 3. Gunicorn (systemd)

```bash
sudo cp deploy/gunicorn.service /etc/systemd/system/nerzhaveyka.service
sudo systemctl daemon-reload
sudo systemctl enable nerzhaveyka
sudo systemctl start nerzhaveyka
```

### 4. Nginx

```bash
sudo cp deploy/nginx.conf /etc/nginx/sites-available/nerzhaveyka
sudo ln -s /etc/nginx/sites-available/nerzhaveyka /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

SSL (Let's Encrypt):

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d nerzhaveyka.kg -d www.nerzhaveyka.kg
```

### 5. Обновление после git push

```bash
chmod +x deploy/update.sh
./deploy/update.sh
```

## Структура

```
core/          — страницы и модели
api/           — REST API и форма заявок
templates/     — HTML-шаблоны
static/        — CSS, JS, изображения
deploy/        — nginx, systemd, скрипт обновления
```

## Контакты

Тел.: +996 998 666 555 / +996 778 666 555  
Email: info@nerzhaveyka.kg
