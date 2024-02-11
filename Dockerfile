FROM ubuntu

MAINTAINER Gokul Methencheri <mgokulm@gmail.com>

RUN apt-get update
RUN apt-get install -y python3-pip python3.7
RUN pip3 install --upgrage pip
RUN pip3 install pipenv


CMD ["echo", "Hello World...! from my first docker image"]