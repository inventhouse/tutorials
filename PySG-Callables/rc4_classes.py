#!/usr/bin/env python3

# classes.py  --  Code + data
# Copyright (c) 2018 Benjamin Holt -- MIT License

from functions import identity_list, key_setup

class Rc4:
    def __init__(self, key, n=256):
        self.state = identity_list(n)
        key_setup(key, self.state)
        self.i = 0
        self.j = 0

    def next_byte(self):
        self.i = (self.i + 1) % len(self.state)
        self.j = (self.j + self.state[self.i]) % len(self.state)
        (self.state[self.i], self.state[self.j]) = (self.state[self.j], self.state[self.i])
        n = (self.state[self.i] + self.state[self.j]) % len(self.state)
        return self.state[n]

    def encrypt_text(self, s):
        return bytes([ b ^ self.next_byte() for b in s.encode() ])

    def decrypt_text(self, s):
        return bytes([ b ^ self.next_byte() for b in s ]).decode()


if __name__ == "__main__":
    key = "asdfg".encode()
    # "6f 6d 0b ab f3 aa 67 19 03 15 30 ed b6 77 ca 74 e0 08 9d d0 e7 b8 85 43 56 bb 14 48 e3 7c db ef e7 f3 a8 4f 4f 5f b3 fd"
    cstest = b'om\x0b\xab\xf3\xaag\x19\x03\x150\xed\xb6w\xcat\xe0\x08\x9d\xd0\xe7\xb8\x85CV\xbb\x14H\xe3|\xdb\xef\xe7\xf3\xa8OO_\xb3\xfd'
    nonce = cstest[:10]
    cipher = cstest[10:]

    rc4 = Rc4(key + nonce)  # WARN: simply adding key + nonce is insecure
    text = rc4.decrypt_text(cipher)
    print(text)

    rc4 = Rc4(key + nonce)  # WARN: simply adding key + nonce is insecure
    plain_text = "This is a test of CipherSaber."
    crypted = rc4.encrypt_text(plain_text)
    print(crypted)
    print(crypted == cipher and "Match" or "No match")
#####
