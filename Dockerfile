FROM python:3
ENV PYTHONUNBUFFERED 1

# sets the working dir
WORKDIR /app/backend

# copies the requirement.txt to workdir root and installs
COPY requirements.txt ./
RUN pip install -r requirements.txt

# copy everything in backend root into docker image
COPY . ./

# exposes port
EXPOSE 33325