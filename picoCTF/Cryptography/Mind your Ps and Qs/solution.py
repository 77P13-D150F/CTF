#!/usr/bin/env python3

# python3 -m pip install pycryptodome
from Crypto.Util.number import inverse, long_to_bytes

# python3 -m pip install primefac
from primefac import primefac

with open('values', 'r') as file:
  enc = file.read().split('\n')

c = enc[1][3:]
n = enc[2][3:]
e = enc[3][3:]

# if the modulo n is too small, it can be factorzed to obtain the primes p and q.
# time of processing can be very long on low end computers.
(p, q) = primefac(n)
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m))
