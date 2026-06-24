#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/var/www/nerzhaveyka"
cd "$APP_DIR"

source venv/bin/activate

git pull origin main
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput
sudo systemctl restart nerzhaveyka

echo "Deploy finished: $(date)"
