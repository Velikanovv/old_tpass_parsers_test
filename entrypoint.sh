#!/bin/sh
#echo "from django.contrib.auth.models import User" > createadmin.py
#echo "User.objects.create_superuser('admin', 'admin@admin.admin', 'admin')" >> createadmin.py
#python manage.py shell < createadmin.py

exec "$@"