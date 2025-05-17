#!/bin/sh

echo "migrate..."
python manage.py migrate

echo "Start Gunicorn..."
exec gunicorn GainMiles.wsgi:application --bind 0.0.0.0:8000