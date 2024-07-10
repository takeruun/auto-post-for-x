FROM python:3.12-alpine

RUN apk update && apk add --no-cache \
  bash \
  build-base \
  gcc \
  libffi-dev \
  musl-dev \
  python3-dev

ENV PYTHONIOENCODING utf-8
ENV TZ="Asia/Tokyo"
ENV LANG=C.UTF-8
ENV LANGUAGE=en_US:en_US

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt
