#!/usr/bin/env python3

import socket

server = ('mercury.picoctf.net', 22342)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server)
        enc = s.recv(1024).decode().split(' \n')

print(''.join([chr(int(i, 0)) for i in enc if i]))
