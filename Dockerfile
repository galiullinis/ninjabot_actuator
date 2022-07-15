FROM python:3.9-slim

USER root
RUN apt-get update && apt-get upgrade
RUN apt-get -y install libpq-dev gcc
RUN mkdir -p /opt/app/ninjabot
WORKDIR /opt/app/ninjabot

COPY ./actuator ./actuator

RUN python -m pip install --upgrade pip
RUN pip install flask psycopg2 waitress paste

ENV PYTHONPATH /opt/app/ninjabot

CMD ["python", "actuator/waitress-server.py"]