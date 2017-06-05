#!/usr/bin/env bash
# Запускаем миграции к БД, параметры подключения к БД берутся из окружения
echo "MIGRATE DATABASE"
ledbillboard migrate

# Стартуем сервер
echo "START uWSGI"
uwsgi --ini /app/tools/uwsgi.ini --die-on-term