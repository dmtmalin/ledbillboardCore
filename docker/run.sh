#!/usr/bin/env bash
# Production config
env SETTINGS_OVERRIDES="/app/config/settings.py"
# Migrates
ledbillboard migrate
# Start uWSGI
uwsgi --ini /app/tools/uwsgi.ini --die-on-term