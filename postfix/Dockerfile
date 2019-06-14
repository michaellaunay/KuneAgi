FROM debian:jessie

RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor postfix rsyslog mailutils sasl2-bin opendkim opendkim-tools && \
  rm -rf /var/lib/apt/lists/*

COPY assets/install.sh /opt/install.sh

VOLUME /var/log
VOLUME /var/spool/postfix

EXPOSE 25

CMD /opt/install.sh;/usr/bin/supervisord -c /etc/supervisor/supervisord.conf
