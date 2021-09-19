
# Dockerfile for worker instances. Able to execute basic python code, nothing more.

FROM python:3.8

COPY workflows/requirements-upd.txt ./
RUN pip install --no-cache-dir -r requirements-upd.txt

RUN mkdir /app
WORKDIR /app

