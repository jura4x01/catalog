FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories &&\
    apk update &&\
    apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev gdal-dev binutils gdal geos-dev &&\
    apk add --update bash &&\
    pip install --no-cache-dir -r requirements.txt &&\
    apk del postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev &&\
    rm -rf /var/cache/apk/*
