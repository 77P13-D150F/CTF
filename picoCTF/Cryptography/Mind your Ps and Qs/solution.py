#!/usr/bin/env python3

# pip install pycryptodome
#from Crypto.Util.number import inverse, long_to_bytes
from Cryptodome.Util.number import inverse, long_to_bytes

#pip install factordb-pycli
from factordb.factordb import FactorDB


def decrypt(p, q, c, e, n):
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    m = pow(c, d, n)
    print(long_to_bytes(m))   # euivalent to: print(bytes.fromhex(hex(m)[2:]))

# If the modulo n is too small, it can be factored to obtain the primes p and q. This process is still long for standard computers. 
# Any online factorization calculator would work (few minutes at least), but the fastest way is to look up at factordb.
# Factordb is a database of known factotizations of any number. 
def lookup(n):
    f = FactorDB(n)
    f.connect()
    return f.get_factor_list()

def main():
    with open('values', 'r') as file:
      enc = file.read().split('\n')

    c = enc[1][3:]
    n = enc[2][3:]
    e = enc[3][3:]
    
    p, q = lookup(n)
    decrypt(p, q, c, e, n)

main()
    
"""
# You can still attempt to factorize with your computer, using primefac module (from primefac import *), there are several sieves and can be executed in parallel.
# Alterantive, here a simple and rough method to sieve through all odd number from square root of n and below.
from math import sqrt

def quick_and_dirty(n):
    p = sqrt(n)
    while p > 1:
        if n % p == 0:
            yield(p, n//p)
        p -= 2
"""
