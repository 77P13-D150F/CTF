#!/usr/bin/env python3

import string


with open('message.txt', 'r') as file:
    msg = file.read()

#print(msg, '\n\n')
az = dict(zip(string.ascii_lowercase, string.ascii_lowercase))

# This challenge can be solved manually, assuming the first part of the last line translates:
# 'zdifIEC'
# 'picoCTF'

# The rest of the alphabet can be rebuilt iterating through the text, changing the values to the az dictionary keys here below.
az['a'] = 'g'
#az['b'] = ''
az['c'] = 'f'
az['d'] = 'i'
az['e'] = 't'
az['f'] = 'o'
az['g'] = 'v'
az['h'] = 'w'
az['i'] = 'c'
az['j'] = 's'
az['k'] = 'd'
az['l'] = 'u'
az['m'] = 'y'
az['n'] = 'q'
az['o'] = 'l'
#az['p'] = '' This letter is part of the flag, so critical to map
az['q'] = 'h'
az['r'] = 'm'
az['s'] = 'e'
az['t'] = 'b'
az['u'] = 'r'
#az['v'] = ''
#az['w'] = ''
az['x'] = 'a'
az['y'] = 'n'
az['z'] = 'p'

missing_letters = 'jkxz'

for i in missing_letters:
    az['p'] = i
    flag = ''
    for i in range(len(msg)):
        if msg[i] in string.ascii_letters:
            if msg[i].isupper():
                flag += az[msg[i].lower()].upper()
            else:
                flag += az[msg[i]]
        else:
            flag += msg[i]

    print('Possible flag:', flag[flag.index(':')+2:])

# The successful flag was picoCTF{FR3QU3NCY_4774CK5_4R3_C001_4871E6FB}
