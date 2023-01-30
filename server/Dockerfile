FROM ubuntu:20.04

WORKDIR /app

#Env for instalation from apache2
ENV TZ=America/Sao_Paulo

ENV DEBIAN_FRONTEND=noninteractive

#Arg for instalation from apache2
RUN  apt-get -y update && apt-get install -y --no-install-recommends apt-utils

#Instalation of the app
RUN apt-get -y install apt-utils apache2 python3 python3-pip libapache2-mod-wsgi-py3 unzip inetutils-ping

#Ativate mod WSGI
RUN a2enmod wsgi

#Copy project from container
COPY /app/ /app

#Copy archives with packets of instalation of the python
COPY requirements.txt /tmp/requirements.txt

#Copy archives from apache2
COPY apache2/test-default.conf /etc/apache2/sites-available/test-default.conf
COPY apache2/test-default.conf /etc/apache2/sites-enabled/test-default.conf
COPY apache2/ports.conf /etc/apache2/ports.conf
# COPY apache2/envvars /etc/apache2/envvars

#Install packets of the python
RUN pip3 install -r /tmp/requirements.txt

ENV DEBIAN_FRONTEND newt

EXPOSE 5500

CMD ["/bin/bash"]

