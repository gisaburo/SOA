#!/bin/bash
LANG=C /sbin/ifconfig |\
awk '/^[a-z]/ {print "[" $1 "]"}
/inet / {print $2}'
