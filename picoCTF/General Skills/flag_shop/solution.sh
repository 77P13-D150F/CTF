#!/usr/bi/bash

# In order to get the flag you need to incraese your account balance above 10000.
# You can achieve it by purchasing an amount of "Definitely not the flag" enough to leak up into the memory stack,
# to override your account balance.
# Logging the sequence of user inputs to display the flag: 2 1 99999999 2 1

nc jupiter.challenges.picoctf.org 9745

exit 0
