#!/usr/bin/env python3

# caesar_closure.py  --  Closures are crazy
# Copyright (c) 2018 Benjamin Holt -- MIT License

# cat caesar_closure_copy.py | pbcopy

"""
0 1 2 3 4 5
--------> a b c d e f g h i j k l m n o p q r s t u v w x y z
a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e


Notes:
- "Inner functions" can use surrounding context *and bring it with them*
- Functions that take functions as parameters
- Functions that return functions
- Code *as* data
"""

# from string import ascii_letters as letters
from string import ascii_lowercase as letters

def make_caesar(shift):
    def shift_letter(letter):
        "Shifts a single letter"
        i = letters.index(letter)
        n = (i + shift) % len(letters)
        return letters[n]

    return shift_letter


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

    caesar5 = make_caesar(5)
    print(encrypt(text, caesar5))

    caesar10 = make_caesar(10)
    print(encrypt(text, caesar10))


#####
