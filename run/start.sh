#/usr/bin/bash
java -Xmx$RAM_LIMIT -javaagent:/app/authlib-injector.jar=$AUTH_SERVER -jar /app/server.jar nogui
