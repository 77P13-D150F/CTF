#!/usr/bin/env python3

import socket

server = ('jupiter.challenges.picoctf.org', 29956)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect(server)
  answer = s.recv(1024).decode().split('\n')[1] + '\n'
  s.sendall(answer.encode())
  # The solution to the first sequence is alrady visible in the text
  
  enc = s.recv(1024).decode().split(' ')
  answer = ''.join([chr(int(i, 8)) for i in enc[enc.index('the') + 2 : enc.index('as')]]) + '\n'
  s.sendall(answer.encode())
  # The second sequence is in octal format
  
  enc = s.recv(1024).decode().split(' ')
  enc = enc[enc.index('the') + 1 : enc.index('as')][0]
  answer = ''.join([chr(int(enc[i:i+2], 16)) for i in range(0, len(enc), 2)]) + '\n'
  s.sendall(answer.encode())
  # The third sequence is in hex format
  
  print(s.recv(1024))
