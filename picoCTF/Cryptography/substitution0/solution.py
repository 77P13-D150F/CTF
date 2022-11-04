#!/usr/bin/env python3

import string


with open('message.txt', 'r') as file:
    msg = file.read()

print(msg, '\n\n')

# The challenge says that the flag is encrypted with a substitution cipher, and the key seems to be at the begin of the ciphertext 
key = msg[:msg.index('\n')-1]

az = dict(zip(key, string.ascii_uppercase))

flag = ''
for i in range(len(msg)):
    if msg[i] in string.ascii_letters:
        if msg[i].islower():
            flag += az[msg[i].upper()].lower()
        else:
            flag += az[msg[i]]
    else:
        flag += msg[i]

print(flag)

