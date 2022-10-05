#!/usr/bin/env python3

from decimal import Decimal

with open('values', 'r') as file:
  enc = file.read().split('\n')

c = Decimal(enc[1][3:])
n = Decimal(enc[2][3:])
e = Decimal(enc[3][3:])

  
