FROM ubuntu:xenial

RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu xenial main" \
  > /etc/apt/sources.list.d/nginx-stable.list \
  && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C300EE8C \
  && apt-get update \
  && apt-get install -y curl supervisor incron nginx-extras vim \
  && apt-get clean \
  && apt-get autoclean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log \
  && rm /etc/nginx/sites-enabled/default \
  && mkdir -p /var/artuser/nginx/sites-enabled \
  && sed -i '1idaemon off;' /etc/nginx/nginx.conf

COPY supervisor.conf /etc/supervisor/conf.d/
COPY nginx.conf /etc/nginx/conf.d/

EXPOSE 80 443 8443

ENTRYPOINT ["/usr/bin/supervisord", "--nodaemon"]
