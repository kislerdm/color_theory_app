FROM python:3.7.4-slim-stretch AS base

WORKDIR /app

COPY . .

RUN python -m pip install --no-cache-dir -r requirements.txt

CMD python run_server.py