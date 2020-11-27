FROM python:3
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

# copy everything in backend root into docker image
COPY . ./

# exposes port
EXPOSE 33325