#!/bin/bash

cd seo_site

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

echo "Server is running on 127.0.0.1:8080/admin"
echo "Login : admin"
echo "Password : root"
