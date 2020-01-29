#!/bin/sh
#########################################################
# info : before installed package python3 and python3-pip
#########################################################
echo "packarge-pip install stating..."
. ./source
for i in ${pip[@]}; do
which $i > /dev/null 2>&1
  if [ $? -ne 0 ]; then
    pip3 install $i 1>/dev/null
    echo "[info] $i installed"
  else
    echo "[info] $i already installed"
  fi
done
echo "packarge-pip install end"
