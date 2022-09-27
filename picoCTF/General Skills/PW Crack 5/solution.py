#!/usr/bin/env python3

from operator import xor

with open('level5.flag.txt.enc', 'rb') as file:
  flag_enc = file.read().decode()

with open('dictionary.txt', 'r') as file:
  keys = file.read()

for key in keys.strip().split('\n'):
  flag = ''.join([chr(xor(ord(flag_enc[i]), ord(key[i % len(key)]))) for i in range(len(flag_enc))])
  if 'picoCTF' in flag:
          print(flag)
