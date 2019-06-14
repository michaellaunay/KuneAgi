all: up

build:
	docker build --pull -t ecreall/postfix .

up:
	docker rm -f postfix 2>/dev/null || true
	docker network create mybridge || true
	mkdir -p /home/docker/volumes/postfix/spool /home/docker/volumes/postfix/log
	mkdir -p /home/docker/volumes/postfix/log/supervisor/
	chown -R root:root assets
	#chown 105:111 assets/domainkeys/*.private
	docker run -p 25:25 -e LOGSPOUT=ignore -e maildomain=$(shell hostname --fqdn) \
      -v /home/docker/volumes/postfix/spool:/var/spool/postfix \
      -v /home/docker/volumes/postfix/log:/var/log \
      -v $(PWD)/assets/domainkeys:/etc/opendkim/domainkeys \
      -v $(PWD)/assets/certs:/etc/postfix/certs \
      --name postfix -d --restart always ecreall/postfix
	docker network connect mybridge postfix

stop:
	docker stop postfix
