#!/usr/bin/env python3

# functions.py  --  Basic funcions are powerful
# Copyright (c) 2018 Benjamin Holt -- MIT License

def identity_list(n=256):
    return list(range(0, n))


def key_setup(key, state):
    "Uses the key (with nonce) to set up a state list in place"
    def mix(i, j):
        "Perform a single ARC4 mixing operation"
        j = (j + key[i % len(key)] + state[i]) % len(state)
        (state[i], state[j]) = (state[j], state[i])
        return j

    j = 0
    for i in range(0, len(state)):
        j = mix(i, j)


if __name__ == "__main__":
    key = "asdfg".encode()
    nonce = b'om\x0b\xab\xf3\xaag\x19\x03\x15'
    # key = "bvebr".encode()
    # nonce = b't\x16[\x96(\xf6\xec\xb1jD'
    # nonce = bytes([ randint(0, 256) for _ in range(0, 10) ])
    # nonce = bytes([ int(h, 16) for h in nonce_hex.split() ])

    state_list = identity_list(16)
    print("State start: {}".format(state_list))

    key_setup(key + nonce, state_list)  # WARN: simply adding key + nonce is insecure
    print("State mixed: {}".format(state_list))


#####
