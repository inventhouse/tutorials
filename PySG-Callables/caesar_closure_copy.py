#!/usr/bin/env python3
# Copyright (c) 2018 Benjamin Holt -- MIT License
# cat caesar_closure_copy.py | pbcopy

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
    text = "hi"
    print(text)

    caesar5 = make_caesar(5)
    print(encrypt(text, caesar5))

    caesar10 = make_caesar(10)
    print(encrypt(text, caesar10))


#####
