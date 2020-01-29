#!/bin/sh
idel_limit=100.0
cpu_idel=$(mpstat 1 5 | tail -n 1 | awk '{print $NF}')
is_alert=$(echo "$cpu_idel < $idel_limit" | bc)
if [ "$is_alert" -eq 1 ]; then
    date_str=$(date '+%Y/%m/%d %H:%M:%S')
    echo "[$date_str] CPU %idle Alert: $cpu_idel (%)"
fi
