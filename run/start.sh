#/usr/bin/bash
echo eula=$EULA > eula.txt
java -Xmx$RAM_LIMIT -javaagent:/app/authlib-injector.jar=$AUTH_SERVER -jar /app/server.jar nogui
