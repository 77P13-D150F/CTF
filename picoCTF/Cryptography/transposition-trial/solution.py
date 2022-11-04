#!/usr/bin/env python3


# The challenge says that every block of 3 got scrambled around, and the first word seems to be three letters long.

with open('message.txt', 'r') as file:
    msg = file.read()

flag = ''
for i in range(0, len(msg), 3):
    block = msg[i:i+3] 
    flag += block[2] + block[0] + block[1]

print(flag)
