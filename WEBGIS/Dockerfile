FROM python:3.6-slim

EXPOSE 5006

ENV PYTHONUNBUFFERED=1
ENV WEBAPP_DIR=/WEBGIS

ADD requirements.txt $WEBAPP_DIR/

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils


RUN apt-get update && \
    apt-get install -y \
        build-essential \
        make \
        gcc \
        locales \
        libgdal20 libgdal-dev
    

RUN mkdir -p /var/log/gunicorn


WORKDIR $WEBAPP_DIR



RUN pip install -r requirements.txt

ADD . $WEBAPP_DIR/