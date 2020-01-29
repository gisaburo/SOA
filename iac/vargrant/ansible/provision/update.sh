#!/bin/sh
echo "os update starting..."
sudo dnf -y update --obsoletes 1>/dev/null
echo "os update end"
