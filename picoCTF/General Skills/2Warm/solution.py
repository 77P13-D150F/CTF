#!/usr/bin/env python3

flag = str(bin(42))[2:]
print(''.join('picoCTF{', flag, '}'))
