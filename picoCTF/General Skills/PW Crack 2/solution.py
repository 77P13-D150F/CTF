#!/usr/bin/env python3

from operator import xor

with open('level2.flag.txt.enc', 'rb') as file:
  flag_enc = file.read().decode()

# The secret key is visible in the python script level2.py
key = chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36)

flag = ''.join([chr(xor(ord(flag_enc[i]), ord(key[i % len(key)]))) for i in range(len(flag_enc))])
print(flag)
