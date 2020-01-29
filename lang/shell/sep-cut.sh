#!/bin/bash
filename="/etc/passwd"
grep -v "^#" "$filename" | cut -f 1 -d ":"
