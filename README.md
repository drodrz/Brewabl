

# Brewabl

Brewable is a brewing app for organizing your brew day.  From recipe creation, to brew day logs, and a handful of handy calculators. It is built with [Python 3.4][0], [Django 1.8][1], the [Django Rest Framework][2], and [AngularJS 1.4+][3].

## Installation

### Django quick start

To set up a django development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    python3 -m venv venv
    . venv/bin/activate

Install all dependencies:

    pip install -r requirements/development.txt

Run migrations:

    python manage.py migrate

Run the server:

    python manage.py runserver

[0]: http://www.python.org/
[1]: http://www.djangoproject.com/
[2]: http://www.django-rest-framework.org/
[3]: http://www.angularjs.org/
