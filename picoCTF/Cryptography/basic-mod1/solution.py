#!/usr/bin/env python3

import string


with open('message.txt', 'r') as file:
    enc_flag = file.read().strip().split(' ')

# Take each number mod 37 and map it to the following character set: 
# 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, 
# and 36 is an underscore.

AZ = dict(zip(range(26), string.ascii_uppercase))
digits = dict(zip(range(26, 36), string.digits))

flag = ''
flag_mod37 = [int(i) % 37 for i in enc_flag]
for i in flag_mod37:
    if i in range(26):
        flag += AZ[i]
    elif i in range(26, 36):
        flag += digits[i]
    else:
        flag += '_'

print(''.join(['picoCTF{', flag, '}']))
