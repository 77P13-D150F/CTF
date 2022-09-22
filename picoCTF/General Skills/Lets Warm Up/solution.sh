#!/usr/bin/bash

flag=$(echo 0x70 | xxd -r -p)
echo "picoCTF{$flag}"
