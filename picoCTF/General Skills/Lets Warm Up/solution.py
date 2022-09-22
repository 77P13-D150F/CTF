#!/usr/bin/env pyhon3

import codecs

flag = str(codecs.decode('0x70'[2:], 'hex'))
print('picoCTF{{0}}'.format(flag))
