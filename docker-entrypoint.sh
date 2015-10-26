#!/bin/bash
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
touch /usr/src/logs/gunicorn.log
touch /usr/src/logs/access.log
tail -n 0 -f /usr/src/logs/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn adl_lrs.wsgi_prod:application \
    --name adl_lrs \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --log-level=info
    --log-file=/usr/src/logs/gunicorn.log \
    --access-logfile=/usr/src/logs/access.log \
    "$@"