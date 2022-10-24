#!/usr/bin/env python3

with open('cipertext', 'r') as file:
  ciphertext = file.read().split('\n')
  
n = int(ciphertext[0][ciphertext[0].index(':')+1])
e = int(ciphertext[1][ciphertext[1].index(':')+1])
c = int(ciphertext[2][ciphertext[2].index(':')+1])
