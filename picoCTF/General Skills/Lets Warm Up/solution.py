#!/usr/bin/env pyhon3

import codecs

flag = str(codecs.decode('0x70'[2:], 'hex'), 'utf-8')
print('picoCTF{{0}}'.format(flag))
