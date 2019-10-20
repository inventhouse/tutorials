# Keeping all the examples in a single file makes them easier to read, edit, and keep consistent with one another; MakeDemo will chunk them out for individual demos.

### header
#!/usr/bin/env python3
# Copyright (c) 2018-2019 Benjamin Holt -- MIT License

### caesar_function
# Basic functions are powerful
"""
a b c d e f g h i j k l m n o p q r s t u v w x y z
|                                                 |
 `-------.                                         `-------.
          |                                                 |
a b c d e f g h i j k l m n o p q r s t u v w x y z|a b c d e
  1 2 3 4 5

--------> a b c d e f g h i j k l m n o p q r s t u v w x y z
a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e

Notes:
- Functions give a name to a snippet of code; take parameters, return results
- Callables can call other callables (incredibly powerful, but easy to take for granted)
- Python allows declaring functions inside other contexts, can use things from surrounding scope (similar to familiar globals)
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

### caesar_class
# Code and data together
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

    text = "that's not got much spam in it"
    print(text)
    print(caesar5(text))

### fibonacci_gen
"""
Notes:
- Generators "magically" group code and "state"
- Written like a function, but using `yield`
- `yield` returns but "picks up where it left off"
- Generators return an iterable; get values with `next()`, `for...in`
- `for...in` is *not* repeatedly calling the "function"; calls it once, iterates over the returned generator
"""

def fibonacci():
    f2 = 1
    yield f2
    f1 = 1
    yield f1
    while True:
        n = f1 + f2
        f2 = f1
        f1 = n
        yield n


print("\nFirst five:")
f = fibonacci()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

print("\nAll you can eat:")
from time import sleep
for n in fibonacci():
    print(n)
    sleep(1)

### random_gen
# Alternate generators example
from time import sleep

def lehmerRng(seed=616089249):
    g = 48271
    n = 2147483647  # 2**31 − 1 (M31)
    x = seed
    while True:
        x = (x * g) % n
        yield x / n


if __name__ == "__main__":
    print("\nThree:")
    r = lehmerRng()
    print(next(r))
    print(next(r))
    print(next(r))

    print("\nAll you can eat:")
    for n in lehmerRng(12345):
        print(n)
        sleep(1)

### caesar_closure
# Closures are crazy
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

### caesar_bound
# Bound methods: instant functions
"""
0 1 2 3 4 5
--------> a b c d e f g h i j k l m n o p q r s t u v w x y z
a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e

Notes:
- "bound methods" let you treat a method (with its instance data) as a "standalone" function
- `instance.method` - *no* parens/args
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

### Vigenère
# The "indecipherable cipher"
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

pyth o npy tho npyt honp yt ho
that's not got much spam in it
ifta'g adr zvh zjaa zdnb gg ph

Notes:
- little bit of everything here
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


def vig_gen(key):
    caesars = []
    for l in key:
        if l in letters:
            n = letters.index(l)
            caesars.append(make_caesar(n))
    while True:
        for c in caesars:
            yield c
        # yield from caesars  # for...in...yield can be shortend to "yield from"


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
