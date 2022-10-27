#!/usr/bin/env python3

import string
from Crypto.Util.number import inverse

with open(r'C:\Users\RDOrsiEl\Downloads\message.txt', 'r') as file:
    enc_flag = file.read().strip().split(' ')

# Take each number mod 41 and find the modular inverse for the result. 
# Then map to the following character set: 1-26 are the alphabet, 
# 27-36 are the decimal digits, and 37 is an underscore.

AZ = dict(zip(range(1, 27), string.ascii_uppercase))
digits = dict(zip(range(27, 37), string.digits))

flag = ''
flag_mod_inverse_41 = [inverse(int(i) % 41, 41) for i in enc_flag]
for i in flag_mod_inverse_41:
    if i in range(1, 27):
        flag += AZ[i]
    elif i in range(27, 37):
        flag += digits[i]
    else:
        flag += '_'

print(''.join(['picoCTF{', flag, '}']))
