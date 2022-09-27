#!/usr/bin/env python3

import base64

enc_flag = b'bDNhcm5fdGgzX3IwcDM1'
flag = base64.b64decode(enc_flag)

print(''.join('picoCTF{', flag.decode(), '}'))
