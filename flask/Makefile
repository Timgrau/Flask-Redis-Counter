SHELL := /bin/bash

run: script start clean

script:
	source write_ip.sh
start:
	sudo docker build -t app_flask .
	sudo docker-compose up
clean:
	sudo docker container rm --force app_flask database_redis
	sudo docker image rm app_flask
	sudo docker network rm bridge0
	sed -i -e '7d' app.py
