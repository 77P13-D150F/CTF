#!/usr/bin/bash

nc mercury.picoctf.net 22342 -i 1 -o flag.log 1>/dev/null 2>/dev/null

while read -r line; do
  printf \\$(printf '%03o' $line)
done < flag.log
