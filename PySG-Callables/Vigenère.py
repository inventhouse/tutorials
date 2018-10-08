#!/usr/bin/env python3

# Vigenère.py  --  The "indecipherable cipher"
# Copyright (c) 2018 Benjamin Holt -- MIT License

"""
--------------------------------------------------------
| a  b c d e f g h i j k l m n o p q r s t u v w x y z |
|--++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--|
| p  q r s t u v w x y z a b c d e f g h i j k l m n o |
| y  z a b c d e f g h i j k l m n o p q r s t u v w x |
| t  u v w x y z a b c d e f g h i j k l m n o p q r s |
| h  i j k l m n o p q r s t u v w x y z a b c d e f g |
| o  p q r s t u v w x y z a b c d e f g h i j k l m n |
| n  o p q r s t u v w x y z a b c d e f g h i j k l m |
--------------------------------------------------------
"""

# from string import ascii_letters as letters
from string import ascii_lowercase as letters

from caesar_closure import make_caesar


def vig_gen(key):
    caesars = []
    for l in key:
        if l in letters:
            n = letters.index(l)
            caesars.append(make_caesar(n))
    while True:
        for c in caesars:
            yield c


class Vig:
    def __init__(self, key):
        "Sets up a Vigenère cipher"
        self.caesars = vig_gen(key)

    def __call__(self, text):
        "Encodes a message by shifting all letters, leaves spaces and punctuation"
        crypt = ""
        for l in text:
            if l in letters:
                l = next(self.caesars)(l)
            crypt += l
        return crypt


if __name__ == "__main__":
    vig = Vig("python")

    text = "that's not got much spam in it"
    print(text)
    print(vig(text))

#####
