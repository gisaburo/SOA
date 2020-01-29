#!/bin/sh
########################################
# before set up ssh-copy-id
########################################
echo "ansible ping starting..."
. ./source
touch ~/hosts # create inventory
for i in ${ipaddr[@]}; do
  ping -c 1 $i > /dev/null 2>&1 # active node check
    if [ $? -eq 0 ]; then
      echo "[Success] ping -> $i"
      grep $i ~/hosts
        if [ $? -ne 0 ]; then
          echo $i >> ~/hosts # insert host ip
        fi
      ansible -i ~/hosts $i -m ping
    else
      echo "[Warning] ping -> $i --Please lunch target node--"
    fi
done
rm ~/hosts # delete inventory
echo "ansible ping end"
