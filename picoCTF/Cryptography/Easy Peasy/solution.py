#!/usr/bin/env python3

import socket
from operator import xor

# Recycling through the same key for multiple messages could lead to decryption.
# the total length of the key is known from the otp.py
KEY_LENGTH = 50000                              
server = ('mercury.picoctf.net', 58913)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server)
        s.recv(1024)
        flag = s.recv(1024).decode().split('\n')[1]
        
        # At begin of the script, the flag is encrypted consuming certain amount of key bytes.
        flag_length = len(bytes.fromhex(flag))
        
        # To reset the key to the begin we need to encrypt a string of null bytes (but could be any type of data) to use all the remaining key length.
        # The remaining key length is obtained by subtracting total key length with the flag length in bytes.
        s.sendall(b''.join([(KEY_LENGTH - flag_length) * b'\x00', b'\n']))
        buffer = s.recv(1024)
        while b'?' not in buffer:
                buffer = s.recv(1024)
        
        # From otp.py we know that the flag is encrypted with one XOR operator.
        # So with the key position now in reset, we send null bytes of the lenght of the flag to obtain the key.
        s.sendall(b''.join([flag_length * b'\x00', b'\n']))
        key = s.recv(1024).decode().split('\n')[1]

        # We finally decrypt the flag by one XOR operation.
        flag = ''.join([str(xor(int(flag[i], 16), int(key[i], 16))) for i in range(len(flag))])

        print(''.join(['picoCTF{', bytes.fromhex(flag).decode(), '}']))
