#!/bin/bash
# Production config
env SETTINGS_OVERRIDES="/app/config/settings.py"
# Collect static
ledbillboard collectstatic --noinput
# Make static folder
mkdir -p /var/www/board/static
# Copy outside
cp /var/www/board/static/* /var/www/board/static
chown -R www-data:www-data /var/www/board/static