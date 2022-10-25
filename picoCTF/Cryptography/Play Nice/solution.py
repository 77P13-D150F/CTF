#!/usr/bin/env python3

server = ('mercury.picoctf.net', 19354)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server)
