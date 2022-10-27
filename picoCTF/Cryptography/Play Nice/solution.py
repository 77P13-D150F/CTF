#!/usr/bin/env python3

import socket


SQUARE_SIZE = 6

# This challenge requires to decrypt a Playfair cipher.
# Here below a set of functions obtained from the file playfair.py to generate a playfair square table.
# I also modified the other functions from the file playfair.py to decrypt rather than encrypt, reversing the process.

def main():
        server = ('mercury.picoctf.net', 19354)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(server)
                data = s.recv(1024).decode().split('\n')
                alphabet = data[0][22:]
                enc_msg = data[1][31:]
                s.recv(1024)

                m = generate_square(alphabet)
                msg = decrypt_string(enc_msg, m)
                s.sendall(''.join([msg, '\n']).encode())
                print(s.recv(1024))
                # Not in standard format, paste as such
                
                
# This funciton is copied from the playfair.py file, it generates the playfair square table
def generate_square(alphabet):
        assert len(alphabet) == pow(SQUARE_SIZE, 2)
        matrix = []
        for i, letter in enumerate(alphabet):
                if i % SQUARE_SIZE == 0:
                        row = []
                row.append(letter)
                if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
                        matrix.append(row)
        return matrix


# This funciton is copied from the playfair.py file, it generates the playfair square table
def get_index(letter, matrix):
        for row in range(SQUARE_SIZE):
                for col in range(SQUARE_SIZE):
                        if matrix[row][col] == letter:
                                return (row, col)
        print("letter not found in matrix.")
        exit()


# Reversing the Playfair encryption process
def decrypt_pairs(pair, matrix):
        p1 = get_index(pair[0], matrix)
        p2 = get_index(pair[1], matrix)
        if p1[0] == p2[0]:
                return matrix[p1[0]][(p1[1] - 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] - 1)  % SQUARE_SIZE]
        elif p1[1] == p2[1]:
                return matrix[(p1[0] - 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] - 1)  % SQUARE_SIZE][p2[1]]
        else:
                return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]

        
# Reversing the Playfair encryption process
def decrypt_string(c, matrix):
        m = ''
        for i in range(0, len(c), 2):
                m += decrypt_pairs(c[i:i + 2], matrix)
        return m


main()
