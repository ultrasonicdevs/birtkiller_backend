#### birtkiller_backend

# ЗАПУСК ДЛЯ РАЗРАБОТКИ

1. Внутри директории `db` скопируйте файл `.env.example` и переименуйте его в `.env`
2. Запустите базу данных командой `docker compose up`
3. Находясь в директории `web` выполните скрипт `autovenv.ps1`
4. Выполните команду `python manage.py runserver` для запуска тестового сервера

## ДОКУМЕНТАЦИЯ ПО API

1. localhost:8000/api/docs
2. localhost:8000/api/swagger
3. localhost:8000/api/redoc
