#!/usr/bin/env python3

c = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']
print(''.join([chr(i + ord('a')-1) if type(i) == int else i for i in c]))
