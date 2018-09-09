ARG VERSION

FROM ubuntu:xenial AS base
LABEL description="Ondo Art Gallery image"

ENV LANG=en_US.UTF-8

RUN echo "deb http://ppa.launchpad.net/deadsnakes/ppa/ubuntu xenial main" \
    > /etc/apt/sources.list.d/deadsnakes-ppa-xenial.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6A755776 \
    && apt-get update \
    && apt-get install build-essential -y \
        rabbitmq-server \
        erlang \
        curl \
        git \
        idn2 \
        locales \
        python3.6 \
        python3.6-dev \
        unzip \
        curl \
        vim \
    && locale-gen en_US.UTF-8 \
    && cd /tmp \
    && curl https://bootstrap.pypa.io/get-pip.py | python3.6 \
    && useradd -ms /bin/bash artuser \
    && usermod -a -G sudo artuser \
    && mkdir -p /home/artuser/dist \
        /home/artuser/dists \
        /var/artuser/static \
        /var/artuser/media \
        /var/artuser/mounts \
        /var/artuser/logs \
        /var/artuser/node_modules \
        /var/artuser/nginx/ssl \
        /var/artuser/nginx/includes \
        /var/artuser/nginx/sites-enabled \
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /tmp/* /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && chown -R artuser:artuser /var/artuser \
    && ldconfig \
    && chown -R artuser:artuser /home/artuser \
    && chmod -R +x /home \
    && chmod -R +x /var

ENV DJANGO_SETTINGS_MODULE=gallery.settings.prod \
    VERSION=${VERSION}

COPY src/ /home/artuser/dist/

RUN apt-get update \
    && cd /home/artuser/dist \
    && python3.6 -m pip install -r /home/artuser/dist/requirements.txt --no-cache-dir \
    && python3.6 -m compileall -f -b /home/hhive/dist \
    && chown -R artuser:artuser /home/artuser

USER artuser
WORKDIR /home/artuser/dist

