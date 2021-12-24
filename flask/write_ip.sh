#!/bin/bash

ipadd=$(sudo docker inspect -f\
'{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' \
database_redis)

sed -i -e "7ihost='$ipadd'" app.py

head app.py
