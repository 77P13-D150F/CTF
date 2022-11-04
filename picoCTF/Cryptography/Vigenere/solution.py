#!/usr/bin/env python3


# The challenge title implies an encryption by Vigenere cipher.
# We also know that the flag is encrypted using the key "CYLAB".

with open('cipher.txt', 'r') as file:
    enc_flag = file.read()

key = 'CYLAB'
key = [ord(i) - ord('A') for i in key]

print(enc_flag)
flag = ''
i = 0
for c in enc_flag:
    if c.islower():
        flag += chr(((ord(c) - ord('a') - key[i % len(key)]) % 26) + ord('a'))
        i += 1
    elif c.isupper():
        flag += chr(((ord(c) - ord('A') - key[i % len(key)]) % 26) + ord('A'))
        i += 1
    else:
        flag += c
print(flag)
