FROM python:latest

ADD app.py /web/
ADD bd_create.sh /web/
ADD requirements.txt /web/
ADD init.sh /web/

RUN pip install --no-cache-dir -r ./web/requirements.txt
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E0C56BD4
RUN echo "deb http://repo.yandex.ru/clickhouse/deb/stable/ main/" | tee /etc/apt/sources.list.d/clickhouse.list
RUN apt-get update
RUN apt-get install -y clickhouse-client
RUN apt-get install -y vim
RUN chmod +x /web/bd_create.sh
RUN chmod +x /web/init.sh

WORKDIR /web/