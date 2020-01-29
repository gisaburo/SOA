#!/bin/bash
script_user="batch1"
if [ $(id -nu) = "$script_user" ]; then
	./bach_program
else
	echo "[ERROR] $script_user ユーザで実行してください" >&2
	exit 1
fi
