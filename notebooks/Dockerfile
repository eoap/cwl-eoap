ARG GDAL=ubuntu-small-3.6.4

FROM ghcr.io/osgeo/gdal:${GDAL} AS gdal

ARG PYTHON_VERSION=3.11

ENV LANG="C.UTF-8" LC_ALL="C.UTF-8"

RUN apt-get update -qq && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    g++ \
    gdb \
    make \
    python3-pip \
    jq \
    python${PYTHON_VERSION} && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir rasterio
