ARG BASE_IMAGE=python:3.9.18-alpine3.17
FROM ${BASE_IMAGE}
COPY . /
RUN pip install -r requirements.txt
ENV MC_HOST=minecraft MC_PORT=25565 MC_DELAY=30
