#!/bin/bash
swapcount_limit=0
swapcount=$(vmstat 1 6 | awk 'NR >= 4 {sum += $7 + $8} END{print sum}' )
if [ "$swapcount" -ge "$swapcount_limit" ]; then
  date_str=$(date '+%Y/%m/%d %H:%M:%S')
  echo "[$date_str] Swap Alert: $swapcount (si+so)"
fi
