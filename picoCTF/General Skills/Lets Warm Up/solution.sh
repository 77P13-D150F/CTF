#!/usr/bin/bash

#flag=$(echo "\x70" | xxd -r -p)
flag=$(echo -e "\x70")

echo "picoCTF{$flag}"
