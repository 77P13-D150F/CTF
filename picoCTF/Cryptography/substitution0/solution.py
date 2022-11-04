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



# This challenge can also be solved manually, assuming the first part of the last line translates:
# 'Pmj tuec xg: fxslSPT'
# 'The flag is: picoCTF'

# Then the rest of the alphabet can be rebuilt iterating through the text, 
# changing the values to the az dictionary keys here below.

#az['a'] = 'q'
#az['b'] = 'r'
#az['c'] = 'g'
#az['d'] = 'm'
#az['e'] = 'a'
#az['f'] = 'p'
#az['g'] = 's'
#az['h'] = 'u'
#az['i'] = 'y'
#az['j'] = 'e'
#az['k'] = 'b'
#az['l'] = 'o'
#az['m'] = 'h'
#az['n'] = 'v'
#az['o'] = 'j'
#az['p'] = 't'
#az['q'] = 'k'
#az['r'] = 'w'
#az['s'] = 'c'
#az['t'] = 'f'
#az['u'] = 'l'
#az['v'] = 'x'
#az['w'] = 'z'
#az['x'] = 'i'
#az['y'] = 'n'
#az['z'] = 'd'

