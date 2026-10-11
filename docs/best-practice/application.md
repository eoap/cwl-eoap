# Prepare the application

This is an optional reference after the [20-minute introduction](../index.md). Start with a command that accepts explicit arguments, runs without prompts, returns a failure status on errors and writes outputs to its working directory.

## Bundle its software

A container image includes the executable and its runtime dependencies. The container notebook uses Python 3.12, pinned Python dependencies and the native `libexpat1` library needed by its rasterio environment:

```dockerfile
FROM docker.io/python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends libexpat1 && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir rasterio==1.5.1 click==8.4.1 pystac==1.15.2 loguru==0.7.3 pyproj==3.7.2 shapely==2.1.2 && python -c "import rasterio"
ADD app.py /app/app.py
ENTRYPOINT []
```

The notebook creates `app.py` before building this image. This cropping application is distinct from the smaller `rio bounds` example.

## Make execution repeatable

Use explicit inputs, write results under the current working directory and avoid relying on host-specific paths. Test with the intended user permissions. Publish shared images to an accessible registry and record an image digest for reproducible releases. Supply data credentials through the execution environment rather than embedding them in an image.

Practise with [01 Command line](https://github.com/eoap/cwl-eoap/blob/main/notebooks/01%20Command%20line.ipynb) and [02 Container](https://github.com/eoap/cwl-eoap/blob/main/notebooks/02%20Container.ipynb). For the normative command-line, container and registry requirements, read the [OGC Best Practice](https://docs.ogc.org/bp/20-089r1.html).
