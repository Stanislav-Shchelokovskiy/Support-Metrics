FROM python:3.10-bullseye

ENV PYTHONBUFFERED=1

# install pyodbc dependency
RUN apt-get update && \
    curl -sSL https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc && \
    curl https://packages.microsoft.com/config/debian/11/prod.list | tee /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \ 
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    ACCEPT_EULA=Y apt-get install -y unixodbc-dev

WORKDIR /root/app

# copy dependencies first to make docker cache it and reuse this cache at the next step
COPY pyproject.toml .

# install app dependencies
RUN curl -sSL https://install.python-poetry.org | python3 - --git https://github.com/python-poetry/poetry.git@master && \
    /root/.local/bin/poetry config virtualenvs.create false && \
    /root/.local/bin/poetry install --only main

# copy app
COPY tasks.py .
COPY worker.py .