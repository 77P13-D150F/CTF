#!/usr/bin/env python3

# Rockstar is a computer programming language designed for creating programs that are also lyrics.
# https://codewithrockstar.com/
# Transpilers are avilable on the community website. Here I used one to convert it into a python script (pip3 install rockstar-py)
# rockstar-py -i lyrics.txt -o lyrics.py did not yield a readable result
# I had success executing lyrics.txt in the online compiler at https://codewithrockstar.com/online

# output of online compiler
lyrics = [114, 114, 114, 111, 99, 107, 110, 114, 110, 48, 49, 49, 51, 114]

flag = ''.join(chr(i) for i in lyrics)
print(''.join(['picoCTF{', flag, '}']))

