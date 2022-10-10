#!/usr/bin/env python3

# pip install pycryptodome
from Crypto.Util.number import inverse, long_to_bytes
#from Cryptodome.Util.number import inverse, long_to_bytes

from primefac import primegen
from math import sqrt

def decrypt(p, q):
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    m = pow(c, d, n)
    print(long_to_bytes(m))

with open('values', 'r') as file:
  enc = file.read().split('\n')

c = enc[1][3:]
n = enc[2][3:]
e = enc[3][3:]

# If the modulo n is too small, it can be factorzed to obtain the primes p and q.
# Time of processing can be very long on low end computers. Any online factorization calculator would also work (few minutes at least).

# Here a simple method to sieve through all odd number from square root of n and below, and attempt to decrypt for all factoring pairs.
p = sqrt(n)
while p > 1:
    if n % p == 0:
        decrypt(p, n//p)
    p -= 2

# Here another example sieving through primes up till square root of n, with primes generated using primefac module
for p in primegen(sqrt(n)):
    if n % p == 0:
        decrypt(p, n/p)
