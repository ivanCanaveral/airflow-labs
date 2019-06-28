FROM ubuntu:disco

ENV AIRFLOW_HOME /home/airflow

RUN apt-get update && \
    apt-get install -y supervisor && \
    apt-get install -y python3 python3-pip

RUN pip3 install apache-airflow

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ADD dags ${AIRFLOW_HOME}/dags

WORKDIR ${AIRFLOW_HOME}

RUN airflow initdb

EXPOSE 8080

CMD ["/usr/bin/supervisord"]