#!/bin/bash

# Migrate database
echo "Migrate database"
python manage.py migrate

# Create superuser
echo "Create superuser"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell

# Starting server
echo "Start runserver"
python manage.py runserver 0.0.0.0:8000