#!/bin/bash
other_user=$(who | wc -l)
if [ "$other_user" -ge 2 ]; then
  echo "[ERROR] whoコマンドの出力が2行以上:作業中のユーザがいます" >&2
  exit 1
fi
commname="/usr/libexec/mysqld"
ps ax -o command | grep -q "^$commname"
if [ $? -eq 0 ]; then
  echo "[ERROR] シャットダウンプロセス中止:プロセス $commname が起動中" >&2
  exit 2
fi
shutdown -h now
