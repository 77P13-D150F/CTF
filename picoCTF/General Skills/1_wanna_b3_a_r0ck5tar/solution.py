#!/usr/bin/env python3

# Rockstar is a computer programming language designed for creating programs that are also lyrics.
# https://codewithrockstar.com/
# Executing lyrics.txt in the online compiler (https://codewithrockstar.com/online) did not succeed.

# I used a transpiler for python in bash (pip3 install rockstar-py): rockstar-py -i lyrics.txt -o lyrics.py
# This lead to the script here below:
"""
Rocknroll = True
Silence = False
a_guitar = 10
Tommy = 44
Music = 170
the_music = input()
if the_music == a_guitar:
    print("Keep on rocking!")
    the_rhythm = input()
    if the_rhythm - Music == False:
        Tommy = 66
        print(Tommy!) B
        Music = 79
        Jamming = 78 
        print(Music!) O
        print(Jamming!) N
        Tommy = 74 
        print(Tommy!) J
        They are dazzled audiences
        print(it!) O
        Rock = 86
        print(it!) V
        Tommy = 73
        print(it!) I
        break
        print("Bring on the rock!")
        Else print("That ain't it, Chief")
        break
"""
# Fixed to yield the flag sequence, wrapped into a function rockstar():
def rockstar():
        seq = []
        Rocknroll = True
        Silence = False
        a_guitar = 10
        Tommy = 44
        Music = 170
        the_music = 10 #input()
        if the_music == a_guitar:
                print("Keep on rocking!")
                the_rhythm = 170 #input()
                if the_rhythm - Music == False:
                        Tommy = 66
                        seq.append(Tommy)
                        Music = 79
                        Jamming = 78
                        seq.extend([Music, Jamming])
                        Tommy = 74
                        seq.append(Tommy)
                        Tommy = 79
                        seq.append(Tommy)
                        Rock = 86
                        seq.append(Rock)
                        Tommy = 73
                        seq.append(Tommy)
                        print("Bring on the rock!")
        else:
                print("That ain't it, Chief") 
        return seq

lyrics = rockstar()

flag = ''.join(chr(i) for i in lyrics)
print(''.join(['picoCTF{', flag, '}']))
