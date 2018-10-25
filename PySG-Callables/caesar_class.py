#!/usr/bin/env python3

# caesar_class.py  --  Code and data together
# Copyright (c) 2018 Benjamin Holt -- MIT License

"""
0 1 2 3 4 5
--------> a b c d e f g h i j k l m n o p q r s t u v w x y z
a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e


Notes:
- Groups code and data
- `__init__` makes a class function-like
- Methods can use instance variables instead of taking everything as parameters
- Implement `__call__` to allow instances to act like functions
"""

# from string import ascii_letters as letters
from string import ascii_lowercase as letters

class Caesar:
    def __init__(self, shift):
        "Sets up a Caesar cipher with a given shift"
        self.shift = shift

    def shift_letter(self, letter):
        "Shifts a single letter"
        i = letters.index(letter)
        n = (i + self.shift) % len(letters)
        return letters[n]

    def __call__(self, text):
        "Encodes a message by shifting all letters, leaves spaces and punctuation"
        crypt = ""
        for l in text:
            if l in letters:
                l = self.shift_letter(l)
            crypt += l
        return crypt


if __name__ == "__main__":
    caesar5 = Caesar(5)

    l = "B"
    print("{} = {}".format(l, caesar5.shift_letter(l)))  # B = G

    text = "that's not got much spam in it"
    print(text)
    print(caesar5(text))

#####
