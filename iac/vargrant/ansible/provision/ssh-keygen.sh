#!/bin/sh
echo "ssh-keygen starting..."
. ./source
if [ ! -e ~/.ssh/$keyfile ]; then
    ssh-keygen -t rsa -f ~/.ssh/$keyfile -N "" # ssh-key create
      if [ $? -eq 0 ]; then
         echo "[Success] ssh-keygen"
      else
         echo "[Failled] ssh-keygen"
         exit
      fi
else
    echo "[info] ssh-key already exist"
fi
echo "ssh-keygen end"
