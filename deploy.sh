#!/usr/bin/env bash

set -e

echo Input server alias
read SERVER

ssh "$SERVER" \
  cd /srv/http/soporte; \
  git pull; \
  source .venv/bin/activate; \
  python manage.py migrate; \
  python manage.py collectstatic; \
  supervisorctl restart soporte:
