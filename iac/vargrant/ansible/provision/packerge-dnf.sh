#!/bin/sh
############################################
# info : cenos need packerge epel-release
############################################
echo "packarge-dnf install stating..."
. ./source
for i in ${dnf[@]}; do
rpm -qa | grep $i > /dev/null 2>&1
  if [ $? -ne 0 ]; then
    sudo dnf -y install $i 1>/dev/null
    echo "[info] $i installed"
  else
    echo "[info] $i already installed"
  fi
done
echo "packarge-dnf install end"
