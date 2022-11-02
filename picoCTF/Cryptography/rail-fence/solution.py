#!/usr/bin/env python3

from collections import deque


with open('message.txt', 'r') as file:
        enc_flag = file.read()

    
# The flag is encrypted using a railfence cipher of 4 rails. First I described the encrypted flag:
L = len(enc_flag)
N = 4
x = 0
find_diagonals = N + ((N - 1) * x)
while find_diagonals < L:
        x += 1
        find_diagonals = N + ((N - 1) * x)
y = find_diagonals - L
K = (L + y) // (2 * (N - 1))
print(f'Encrypted flag: {enc_flag}\nLength L: {L}\nRails N: {N}\nDiagonals x: {x}\nTail pad y: {y}\nCycle key K: {K}\n')

# Then I split the ciphertext in 4 rails, and added the tail pad. I tested manually the right offsets of K, but can also be brute forced:
one = deque(enc_flag[:K+1])
two = deque(enc_flag[K+1:K*3+2])
three = deque(enc_flag[K*3+2:K*5+2])
four = deque(enc_flag[K*5+2:])

if y > 0:
        four.append(' ')
        y -= 1
        if y > 0:
                three.append(' ')
                y -= 1
                if y > 0:
                        two.append(' ')

print('Ciphertext rails:')
print(len(one), one)
print(len(two), two)
print(len(three), three)
print(len(four), four)

# I used deque.popleft() to rebuild the flag.
flag = ''
while True:
        try:
                flag += one.popleft()
                flag += two.popleft()
                flag += three.popleft()
                flag += four.popleft()
                flag += three.popleft()
                flag += two.popleft()
        except IndexError:
                print(flag)
                break
              
