FROM python:3.6-slim


ENV PYTHONUNBUFFERED=1
ENV BOKEH_DIR=/


RUN apt-get update && apt-get install -y bash libpq-dev gcc

COPY requirements.txt /requirements.txt

COPY app/ /app

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        make \
        gcc \
        locales \
        libgdal20 libgdal-dev && \
    python -m pip install numpy cython --no-binary numpy,cython && \
    python -m pip install \
        "rasterio>=1.0a12" fiona shapely \
        --pre --no-binary rasterio,fiona,shapely && \
    python -m pip install -r /requirements.txt && \
    python -m pip uninstall -y cython && \
    rm -r /root/.cache/pip && \
    apt-get remove -y --purge libgdal-dev make gcc build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /

RUN pip install -r requirements.txt

