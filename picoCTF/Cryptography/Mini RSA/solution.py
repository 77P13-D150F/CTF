#!/usr/bin/env python3

with open('cipertext', 'r') as file:
  enc_flag = file.read().split('\n')
  
n = int(enc_flag[0][enc_flag[0].index(':')+2:])
e = int(enc_flag[1][enc_flag[1].index(':')+2:])
c = int(enc_flag[3][enc_flag[3].index(':')+2:])
