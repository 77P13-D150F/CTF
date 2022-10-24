#!/usr/bin/env python3

import socket


server = ('mercury.picoctf.net', 2671)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server)
