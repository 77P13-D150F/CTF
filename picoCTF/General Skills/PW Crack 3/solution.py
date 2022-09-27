#!/usr/bin/env python3

from operator import xor

with open('level3.flag.txt.enc', 'rb') as file:
  flag_enc = file.read().decode()
  
# The secret key is one of the items in this list, pasted from level3.py
keys = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]

# The level3.py file compares each key to a hash reference before executing the xor operation.
# As there are only 7 of them we can simply bruteforce
for key in keys:
  flag = ''.join([chr(xor(ord(flag_enc[i]), ord(key[i % len(key)]))) for i in range(len(flag_enc))])
  print(flag)
