#!/usr/bin/env bash
# Production config
env SETTINGS_OVERRIDES="/app/config/settings.py"
exec "$@"