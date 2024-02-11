FROM ubuntu

MAINTAINER Gokul Methencheri <mgokulm@gmail.com>

RUN apt-get update

CMD ["echo", "Hello World...! from my first docker image"]