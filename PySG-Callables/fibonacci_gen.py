#!/usr/bin/env python3
# Copyright (c) 2018 Benjamin Holt -- MIT License
# cat fibonacci_gen.py | pbcopy

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

#####
