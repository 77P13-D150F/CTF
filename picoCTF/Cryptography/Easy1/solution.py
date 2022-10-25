#!/usr/bin/env python3

enc_flag = 'UFJKXQZQUNB'
key = 'SOLVECRYPTO'

# From the file table.txt we see that this is a Vigenere cipher
flag = ''.join([chr(((ord(c) - ord(key[i % len(key)]) - 2 * ord('A')) % 26) + ord('A')) for i, c in enumerate(enc_flag)])
print(''.join(['picoCTF{', flag, '}']))
