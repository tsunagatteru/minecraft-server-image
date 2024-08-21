ARG BUILD_IMAGE=python:3.9.18-alpine3.17
ARG BASE_IMAGE=eclipse-temurin:22-jre-alpine
FROM ${BUILD_IMAGE} AS builder
COPY build/* /
RUN pip install -r requirements.txt
WORKDIR /build
ARG MINECRAFT_VERSION="1.21"
RUN python3 /dlServer.py $MINECRAFT_VERSION
ARG AUTHLIB_VERSION="1.2.5"
RUN wget -O authlib-injector.jar \
	https://github.com/yushijinhun/authlib-injector/releases/download/v$AUTHLIB_VERSION/authlib-injector-$AUTHLIB_VERSION.jar
FROM ${BASE_IMAGE}
RUN apk add screen
RUN mkdir /mc-server
COPY --from=builder --chmod=0755 /build/* /app/
COPY --chmod=0755 run/* /app/
WORKDIR /data
ENV RAM_LIMIT=2G AUTH_SERVER=ely.by EULA=true
STOPSIGNAL SIGTERM
EXPOSE 25565
CMD ["/app/start.sh"]
