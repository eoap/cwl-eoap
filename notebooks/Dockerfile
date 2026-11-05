ARG GDAL=ubuntu-small-3.13.3
FROM ghcr.io/osgeo/gdal:${GDAL} AS gdal

ENV LANG="C.UTF-8" LC_ALL="C.UTF-8"

# Refresh trust and isolate Python packages from the distro-managed interpreter.
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates g++ gdb make jq python3-venv && \
    sed -i '/^[#!]*mozilla\/emSign_ECC_Root_CA_-_G3\.crt$/s/^[#!]*/!/' /etc/ca-certificates.conf && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
RUN python -m pip install --no-cache-dir --upgrade "pip @ https://files.pythonhosted.org/packages/3f/06/3e4420302363fbb71be3c7f35ce042f54bfca330e3e66b3a2e3c4cca579f/pip-26.2.2-py3-none-any.whl#sha256=fd7f4dfa8190e014013b9f08f3e973f4e4c26ffd179a204895533a7254813a70" && \
    python -m pip install --no-cache-dir "certifi>=2026.10.19" rasterio
