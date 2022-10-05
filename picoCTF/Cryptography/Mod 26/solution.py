#!/usr/bin/env python3

import string
from collections import deque

# To obtain the flag apply ROT13 to the string cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}
enc = 'cvpbPGS{arkg_gvzr_V\'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}'

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


print(encrypt(13, enc))
