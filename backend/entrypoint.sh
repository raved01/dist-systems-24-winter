#!/bin/bash

# Führe Migrationen aus
python manage.py makemigrations
python manage.py migrate

# Starte den Server
exec python manage.py runserver 0.0.0.0:80