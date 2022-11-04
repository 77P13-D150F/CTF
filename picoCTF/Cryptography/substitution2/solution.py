#!/usr/bin/env python3


import string

def decrypt(msg, az):
    flag = ''
    for i in range(len(msg)):
        if msg[i] in string.ascii_letters:
            if msg[i].isupper():
                flag += az[msg[i].lower()].upper()
            else:
                flag += az[msg[i]]
        else:
            flag += msg[i]
    return flag



def main():
    with open('message.txt', 'r') as file:
        msg = file.read()
    
    #print(msg, '\n\n')
        
    az = dict(zip(string.ascii_lowercase, string.ascii_lowercase))
    
    # This challenge can be solved manually, assuming a segment of the message tail translates:
    # 'pemzMGN'
    # 'picoCTF'
    
    # Then the rest of the alphabet can be rebuilt iterating through the text, 
    # changing the values to the az dictionary keys here below.
    
    az['a'] = 'v'
    az['b'] = 'm'
    az['c'] = 'g'
    #az['d'] = ''
    az['e'] = 'i'
    az['f'] = 'b'
    az['g'] = 't'
    az['h'] = 'n'
    az['i'] = 'd'
    az['j'] = 'e'
    az['k'] = 'w'
    #az['l'] = ''
    az['m'] = 'c'
    az['n'] = 'f'
    az['o'] = 'x'
    az['p'] = 'p'
    az['q'] = 'a'
    az['r'] = 'y'
    az['s'] = 'u'
    #az['t'] = ''
    az['u'] = 's'
    az['v'] = 'h'
    az['w'] = 'r'
    az['x'] = 'l'
    #az['y'] = ''
    az['z'] = 'o'

    flag = decrypt(msg, az)
    print(flag[flag.index('picoCTF'):])
    

main()
