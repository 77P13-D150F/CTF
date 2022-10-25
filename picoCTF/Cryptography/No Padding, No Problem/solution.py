#!/usr/bin/env python3

import socket
from Crypto.Util.number import long_to_bytes

server = ('mercury.picoctf.net', 2671)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server)
        s.recv(1024)
        data = s.recv(1024).decode().split('\n')
        n = int(data[4][3:])
        e = int(data[5][3:])
        c = int(data[6][12:])

        # RSA is homomorphic, so it is possible to append a new plaintext k to the ciphertext c,
        # so to obtain an new ciphertext c1, by applying the formula c1 = c * pow(k, e, n)
        # Let's chose a simple value of k (e.g. k = 2) and submit c1 to the oracle for decryption.
        k = 2
        c1 = c * pow(k, e, n)
        s.sendall(''.join([str(c1), '\n']).encode())
        m1 = int(s.recv(1024)[13:])
        
        # Now m1 = pow(c1, d, n),
        # but as there is no padding in the encryption it is also true that m1 = (k * m) % n
        m = (m1 // k) % n
        print(long_to_bytes(m))
