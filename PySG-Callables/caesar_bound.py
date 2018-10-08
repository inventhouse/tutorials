#!/usr/bin/env python3

# caeser_function.py  --  Basic functions are powerful
# Copyright (c) 2018 Benjamin Holt -- MIT License

"""
0 1 2 3 4 5
--------> a b c d e f g h i j k l m n o p q r s t u v w x y z
a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e
"""


# from string import ascii_letters as letters
from string import ascii_lowercase as letters

class Caesar:
    def __init__(self, shift):
        "Sets up a Caesar cipher with a given shift"
        self.shift = shift

    def shift_forward(self, letter):
        "Shifts a single letter forward through the alphabet (generally encrypting)"
        i = letters.index(letter)
        n = (i + self.shift) % len(letters)
        return letters[n]

    def shift_backward(self, letter):
        "Shifts a single letter backward through the alphabet (generally decrypting)"
        i = letters.index(letter)
        n = (i - self.shift) % len(letters)
        return letters[n]


def encrypt(text, cipher):
    "Encrypts all letters in text with the cipher function, leaves spaces and punctuation"
    crypt = ""
    for l in text:
        if l in letters:
            l = cipher(l)
        crypt += l
    return crypt


if __name__ == "__main__":
    text = "that's not got much spam in it"
    print(text)

    caesar5 = Caesar(5)
    crypt = encrypt(text, caesar5.shift_forward)
    print(crypt)
    plain = encrypt(crypt, caesar5.shift_backward)
    print(plain)

#####
