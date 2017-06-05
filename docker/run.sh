#!/usr/bin/env bash
# Migrates
ledbillboard migrate
# Start uWSGI
uwsgi --ini /app/tools/uwsgi.ini --die-on-term