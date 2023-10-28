#/usr/bin/bash
java -Xmx$RAM_LIMIT -javaagent:authlib-injector.jar=$AUTH_SERVER -jar server.jar nogui
