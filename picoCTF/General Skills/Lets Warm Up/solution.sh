#!/usr/bin/bash

#flag=$(echo "\x70" | xxd -r -p)
#flag=$(echo -e "\x70")
#flag=echo "16i 0x70 P" | dc
flag=printf "\x70"

echo "picoCTF{$flag}"
