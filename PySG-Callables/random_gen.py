#!/usr/bin/env python3

# random_gen.py  --  Generators example
# Copyright (c) 2018 Benjamin Holt -- MIT License

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

#####
