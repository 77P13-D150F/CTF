#!/usr/bin/env python3

import string


ALPHABET = string.ascii_lowercase[:16]


def reverse_shift(c, k):
	t1 = ord(c) + ord("a")
	t2 = ord(k) + ord("a")
	return ALPHABET[(t1 - t2) % len(ALPHABET)]


def b16_decode(enc):
    return ''.join([chr(int('{0:04b}'.format(ALPHABET.index(enc[i])) + '{0:04b}'.format(ALPHABET.index(enc[i+1])), 2)) for i in range(0, len(enc)-1, 2)])


def brute_force_single_character_key(c):
    for key in ALPHABET:
        flag = b16_decode(''.join([reverse_shift(j, key[i % len(key)]) for i, j in enumerate(c)]))
        ord_flag = [ord(i) for i in flag]
        if min(ord_flag) > 24 and max(ord_flag) < 128:
            print(f'Decryption successful with key {key}')
            return flag
    print('Brute force not successful')
    return None

  
def main():    
    c = 'lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhiji' 
    print(brute_force_single_character_key(c))

main()
