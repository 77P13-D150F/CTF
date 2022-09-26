#!/usr/bin/env python3

# I pasted the encrypted flag from the convertme.py file. The secret key is also in the file.
# You can also run the python script and look up online for a binary conversion of the random integer it displays.

key = 'enkidu'
flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5f) + chr(0x05) + chr(0x08) + chr(0x2a) + chr(0x1c) + chr(0x5e) + chr(0x1e) + chr(0x1b) + chr(0x3b) + chr(0x17) + chr(0x51) + chr(0x5b) + chr(0x58) + chr(0x5c) + chr(0x3b) + chr(0x42) + chr(0x57) + chr(0x5c) + chr(0x0d) + chr(0x5f) + chr(0x06) + chr(0x46) + chr(0x5c) + chr(0x13)

# one liner
flag = ''.join([chr(xor(ord(flag_enc[i]), ord(key[i % len(key)]))) for i in range(len(flag_enc))])

# expanded
flag = ''
for i in range(len(flag_enc)):        # index through all the encrypted flag
  k = key[i % len(key)]               # assing the letter of the key at the right index, it rotates through the letters of the key
  j = flag_enc[i]                     # assign the letter of the encrypted flag at the same index
  flag += chr(xor(ord(j), ord(k)))

print(flag)
