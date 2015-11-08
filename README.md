# Brewabl

Brewabl is a brewing web app for organizing your brew day.  From recipe creation, to brew day logs, and a handful of handy calculators.  This site aspires to combine Beersmith's power and versatility with Brewtoad's ease of use.  The backend is powered by [Python 3.4][0], [Django 1.8][1], the [Django Rest Framework][2], while the frontend is written in [AngularJS 1.4+][3].

## Installation

### Django backend quick start

To set up a django development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    cd backend
    python3 -m venv venv
    . venv/bin/activate

Install all dependencies:

    pip install -r requirements/development.txt

Run migrations:

    python manage.py makemigrations
    python manage.py migrate

Run the server:

    python manage.py runserver

### Angular frontend quick start

To set up a angular development environment, you'll first need
npm installed.  Use that to install Bower and Grunt.

    npm install -g bower grunt

Install all dependencies and packages:
    
    cd frontend
    npm install
    bower install

### Running the site

To run the site locally, you'll need to provide a server[4] for serving up the
angular frontend via index.html, and routing any api and authentication calls
to the django server.

Or, visit the lastest version at www.brewabl.com

## Features

Not many.  Currently just working on the underlying framework.  Maybe a few handy calculators soon(tm).

## Roadmap

- Recipe Formulation + management
- Brewday timer + note taking
- Equipment Manager
- Yeast Starter
- Water chemistry
- BeerXML Support
- etc...


[0]: http://www.python.org/
[1]: http://www.djangoproject.com/
[2]: http://www.django-rest-framework.org/
[3]: http://www.angularjs.org/
[4]: http://nginx.org/en/
