#!/usr/bin/env python3

import string
from collections import deque


def encrypt(rot, text):
    az_deque = deque([l for l in string.ascii_lowercase])                            
    az_deque.rotate(rot)
    new_alphabet = ''.join(az_deque)
                                                                  
    rot_tab = text.maketrans(string.ascii_lowercase, new_alphabet)                   
    cipher = text.translate(rot_tab)                                                 
    
    AZ_deque = deque(string.ascii_uppercase)                                         
    AZ_deque.rotate(rot)
    new_alphabet = ''.join(AZ_deque)
    
    rot_tab = cipher.maketrans(string.ascii_uppercase, new_alphabet)
    return cipher.translate(rot_tab)


def main():
    with open('ciphertext', 'r') as file:
        enc_flag = file.read()
        
    for i in range(26):
        flag = encrypt(i, enc_flag)
        if 'pico' in flag:
            print(flag)

main()
