
# Coders-HQ Backend

This repository holds the Coders-HQ backend. It is made using [Django](https://www.djangoproject.com/) and [Postgres](https://www.postgresql.org/) as an API backend to the Coders-HQ frontend which is hosted on another repository.

## Database

Django should be connected to postgres (postgres can be installed locally or using docker) but there is an option to use sqlite for development. Although sqlite should not be used for release. To switch between sqlite or postgres change `DATABASES = ...` in settings.py

Docker makes it easy to set up postgres. The docker-compose.yaml file creates and connects the two containers (django+postgres) together, you can also create postgres by itself and connect to django which you build locally.

## Building

### Pre requisites

1.  python 3
1.  Pip
3.  (optional) pipenv
2.  (Optional) docker

### Building locally

1.  Run `pip install -r requirements.txt`
1.  Make sure you have the correct Database in the settings.py
1.  Run `python manage.py runserver 0.0.0.0:33325`
1.  On a web browser open localhost:33325

### Building on Docker

1.  make sure you have the correct Database in settings.py
3.  Run `docker-compose up` in root dir and it will create the django and postgres apps, it will also run the web app
1.  On a web browser open localhost:33325

