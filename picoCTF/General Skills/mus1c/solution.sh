#!/usr/bin/bash

# Rockstar is a computer programming language designed for creating programs that are also lyrics.
# https://codewithrockstar.com/
# Transpilers are avilable on the community website. Here I used one to convert it into a python script (pip3 install rockstar-py)

rockstar-py -i lyrics.txt -o lyrics.py
chmod +x lyrics.py

exit 0
