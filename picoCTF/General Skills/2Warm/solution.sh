#!/usr/bin/bash

flag=$(echo "obase=2; 42" | bc)
echo "picoCTF{$flag}"

exit 0
