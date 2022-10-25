#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes
import gmpy2


with open(r'H:\04_Python\ciphertext', 'r') as file:
    enc_flag = file.read().split('\n')

n = int(enc_flag[0][enc_flag[0].index(':')+2:])
e = int(enc_flag[1][enc_flag[1].index(':')+2:])
c = int(enc_flag[3][enc_flag[3].index(':')+2:])


# The challenge says that the plaintext is padded so that (m ** e) is just barely larger than n.
# So if pow(m, e) % (n * pad) = c, then pow(m, e) = pad * n + c, then we can obtain the flag by
# screening through a pad range until m is a true root of pow(pad * n + c, e).

MAX_PAD = 10000

for pad in range(MAX_PAD):
    print(f'\rPadding {pad} of {MAX_PAD}', end='\r', flush=True)
    m, true_root = gmpy2.iroot(pad * n + c, e)
    if true_root:
        print(f'\n{long_to_bytes(m).strip().decode()}')
        break 
