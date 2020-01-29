#!/bin/bash
echo "ssh-copy-id starting..."
. ./source
for i in ${ipaddr[@]}; do # loop ipaddr
  ping -c 1 $i > /dev/null 2>&1 # active node check
    if [ $? -eq 0 ]; then
      echo "[Success] ping -> $i"
      ssh-keygen -R $i > /dev/null 2>&1 # delete known_hosts
      sshpass -p $password ssh-copy-id -o StrictHostKeyChecking=no -i ~/.ssh/${keyfile}.pub ${user}@$i # ssh-copy-id
        if [ $? -eq 0 ]; then
          echo "[Success] ssh-copy-id"
        else
          echo "[Failled] ssh-copy-id"
          exit
        fi
    else
      echo "[Warning] ping -> $i --Please lunch target node--"
  fi
done
echo "ssh-copy-id end"
