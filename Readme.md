
## Building

### Pre requisites

1.  You need python 3
1.  Pip
3.  (optional) pipenv
2.  (Optional) docker (Windows 10 pro/linux/Mac)

### Building locally

2.  Run `pip install -r requirements.txt`
1.  Make sure you have the correct Database in the settings.py
1.  Run `python manage.py runserver 0.0.0.0:33325`
1.  On a web browser open localhost:33325

### Building on Docker

1.  make sure you have the correct Database in settings.py
3.  Run `docker-compose up` in root dir and it will create the django app and the postgres, it will also run the web app
1.  On a web browser open localhost:33325

