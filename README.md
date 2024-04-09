# Quick-Polling-App

mkdir polling_project
cd polling_project

Create a virtual enviroment

python -m venv venv

Activate Virtual venv
venv\Scripts\activate

Install Django and other
pip install django django-jquery django-crispy-forms

Django project named "polling_project":
django-admin startproject polling_project .

Create a new Django application named "polls":
python manage.py startapp polls

Open polling_project/settings.py and add 'polls', 'crispy_forms' to the INSTALLED_APPS list:
INSTALLED_APPS = [

CRISPY_TEMPLATE_PACK = 'bootstrap4'

{% load crispy_forms_tags %}

'django_jquery' middleware is added to the MIDDLEWARE list in polling_project/settings.py:

MIDDLEWARE = [

    'django_jquery.middleware.jQueryMiddleware',
]

Run migrations to create necessary database tables:
python manage.py migrate

