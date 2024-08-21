#!/bin/sh
trap 'stop_server' SIGTERM

stop_server() {
	echo "Stopping Minecraft server..."
	screen -p 0 -S minecraft -X stuff "stop\015"
	while screen -list | grep -q "minecraft"; do
		sleep 1
	done
	echo "Minecraft server stopped."
	exit 0
}

echo eula=$EULA > eula.txt
screen -L -Logfile /app/screen-log -dmS minecraft java -Xmx$RAM_LIMIT -javaagent:/app/authlib-injector.jar=$AUTH_SERVER -jar /app/server.jar nogui
while ! screen -list | grep -q "minecraft"; do
	sleep 1
done
tail -f /app/screen-log & wait ${!}
