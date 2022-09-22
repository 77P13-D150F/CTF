#!/usr/bin/bash

flag=$(echo "obase=10; ibase=16; 3D" | bc)
#flag=$(echo $((16#3D)))

echo "picoCTF{$flag}"

