#!/bin/bash
if [ ! -f "$1" ]; then
  echo "対象のパッケージリストファイルが存在しません: $1" >&2
  exit 1
fi
pkglist=$(cat "$1")
rpm -q $pkglist --queryformat '%{INSTALLTIME:date} : %{NAME}\n'
