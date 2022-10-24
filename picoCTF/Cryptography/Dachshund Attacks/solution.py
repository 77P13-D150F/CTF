#!/usr/bin/env python3

import socket
import owiener
from Crypto.Util.number import long_to_bytes


server = ('mercury.picoctf.net', 62786)

# The challenge implies that the private key (d) of this RSA encryption is too small. 
# The Wiener attack works fine, the Boneh and Durfee attack does also work.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server)
        s.recv(1024)
        s.recv(1024)
        e = int(s.recv(1024).decode()[3:])
        nc = s.recv(1024).decode().split('\n')

n = int(nc[1][3:])
c = int(nc[2][3:])

d = owiener.attack(e, n)
m = pow(c, d, n)
print(long_to_bytes(m))
