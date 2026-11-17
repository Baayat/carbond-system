#!/usr/bin/env bash
# exit on error
set -o errexit

cd Car_Django

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Automatically ensure superuser admin exists on Render
python -c "
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Core.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
username = os.environ['ADMIN_USERNAME']
email = os.environ['ADMIN_EMAIL']
password = os.environ['ADMIN_PASSWORD']
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Superuser created successfully')
else:
    u = User.objects.get(username=username)
    u.email = email
    u.set_password(password)
    u.is_superuser = True
    u.is_staff = True
    u.save()
    print('Superuser updated successfully')
"