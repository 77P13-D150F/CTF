#!/usr/bin/env pyhon3

import codecs

#flag = str(codecs.decode('0x70'[2:], 'hex'), 'utf-8')
flag = chr(int('0x70', 16))

print('picoCTF{' + flag + '}')
