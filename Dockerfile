FROM python:3.11.6-alpine3.18

WORKDIR /app

COPY . /app

RUN  pip install --no-cache-dir -r /app/requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000