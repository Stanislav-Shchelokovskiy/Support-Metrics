FROM python:3.10-bullseye

ENV PYTHONBUFFERED=1

WORKDIR /root/app

RUN apt-get update && \
    apt-get -y install \
        netcat

# copy dependencies first to make docker cache it and reuse this cache at the next step
COPY ./pyproject.toml /root/app/

# install app dependencies
RUN curl -sSL https://install.python-poetry.org | python3 - --git https://github.com/python-poetry/poetry.git@master && \
    /root/.local/bin/poetry config virtualenvs.create false && \
    /root/.local/bin/poetry install --only main

# copy app
COPY . /root/app