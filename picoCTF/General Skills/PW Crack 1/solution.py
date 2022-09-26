#!/usr/bin/env python3

from operator import xor


with open('level1.flag.txt.enc', 'rb') as file:
  flag_enc = file.read().decode()
 
# The secret key is visible in the python script level1.py
key = '8713'

flag = ''.join([chr(xor(ord(flag_enc[i]), ord(key[i % len(key)]))) for i in range(len(flag_enc))])
print(flag)
