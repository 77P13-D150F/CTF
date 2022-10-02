#!/usr/bin/env python3

import socket
import hashlib

server = ('saturn.picoctf.net', 54555)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server)
        word = s.recv(1024).split(b'\'')[1]
        answer = hashlib.md5(word).hexdigest() + '\n'
        s.sendall(answer.encode())

        s.recv(1024)
        word = s.recv(1024).split(b'\'')[1]
        answer = hashlib.md5(word).hexdigest() + '\n'
        s.sendall(answer.encode())

        s.recv(1024)
        word = s.recv(1024).split(b'\'')[1]
        answer = hashlib.md5(word).hexdigest() + '\n'
        s.sendall(answer.encode())

        s.recv(1024)
        print(s.recv(1024).split(b'\n')[1])
