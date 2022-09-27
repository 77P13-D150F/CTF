#!/usr/bin/bash

nc -i 1 jupiter.challenges.picoctf.org 4427 > log.txt
cat log.txt | grep picoCTF

exit 0
