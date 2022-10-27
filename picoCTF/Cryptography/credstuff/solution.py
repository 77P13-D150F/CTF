#!/usr/bin/env python3

import tarfile
from pprint import pprint
import string
from collections import deque

# Find the password of the user cultiris and decrypt it from the leak.tar file.
# The first user in usernames.txt corresponds to the first password in passwords.txt.
# The second user corresponds to the second password, and so on.


def caesar(rot, text):
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
       
        with tarfile.open('leak.tar') as tar:
                tar.extractall()

        with open('leak/usernames.txt', 'r') as file:
                users = file.read().split('\n')

        with open('leak/passwords.txt', 'r') as file:
                passwords = file.read().split('\n')

        USER = 'cultiris'
        database = dict(zip(users, passwords))
        #pprint(database)
        enc_flag = database[USER]         # It is a Caesar cipher
        for i in range(26):
                flag = caesar(i, enc_flag)
                if 'pico' in flag:
                        print(flag)

main()
