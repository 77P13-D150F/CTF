#!/usr/bin/env python3

import socket


server = ('mercury.picoctf.net', 19354)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server)
        data = s.recv(1024).decode().split('\n')
        alphabet = data[0][22:]
        message = data[1][31:]
