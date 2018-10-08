#!/usr/bin/env python3

# caeser_function.py  --  Basic functions are powerful
# Copyright (c) 2018 Benjamin Holt -- MIT License

"""
a b c d e f g h i j k l m n o p q r s t u v w x y z
|                                                 |
 `-------.                                         `-------.
          |                                                 |
a b c d e f g h i j k l m n o p q r s t u v w x y z|a b c d e
  1 2 3 4 5

--------> a b c d e f g h i j k l m n o p q r s t u v w x y z
a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e
"""


from string import ascii_lowercase as letters

def caesar(text, shift):
    "Encodes a message by shifting all letters, leaves spaces and punctuation"

    def shift_letter(letter):
        "Shifts a single letter"
        i = letters.index(letter)
        n = (i + shift) % len(letters)
        return letters[n]

    crypt = ""
    for l in text:
        if l in letters:
            l = shift_letter(l)
        crypt += l
    return crypt


if __name__ == "__main__":
    text = "that's not got much spam in it"
    print(text)
    print(caesar(text, 5))

#####
