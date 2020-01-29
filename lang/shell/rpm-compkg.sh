#!/bin/bash
if [ ! -f "$1" ]; then
  echo "ファイルがありません: $1" >&2
  exit 2
fi
pkgname=$(rpm -qf "$1")
if [ $? -eq 0 ]; then
  echo "$1 -> $pkgname"
else
  echo "$1 はパッケージに属していません" >&2
  exit 1
fi
