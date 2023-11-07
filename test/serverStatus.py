from mcstatus import JavaServer
import os
import sys
import time

def main():
    latency = -1
    server = JavaServer.lookup(os.environ['MC_HOST']+":"+os.environ['MC_PORT'])
    time.sleep(int(os.environ['MC_DELAY']))
    try:
        latency = server.ping()
    except:
        print("Connection refused")
        sys.exit(1)
    else:
        print(f"The server replied in {latency} ms")
        sys.exit(0)

if __name__ == "__main__":
    main()
