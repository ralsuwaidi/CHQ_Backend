FROM python:3 AS worker
ENV PYTHONUNBUFFERED 1

# sets the working dir
WORKDIR /app/backend

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PIPENV_HIDE_EMOJIS=1

# copies the requirement.txt to workdir root and installs
COPY Pipfile Pipfile.lock ./
RUN set -ex && pip install pipenv --upgrade
RUN set -ex && pipenv install --system
RUN pip install gunicorn
RUN pip install django-heroku

# copy everything in backend root into docker image
COPY . ./

RUN python manage.py makemigrations && python manage.py migrate

EXPOSE 33325