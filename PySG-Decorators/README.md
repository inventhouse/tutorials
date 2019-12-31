
Decorators, how do they work??
==============================
Spoiler: They're **not** magic!

Well, maybe just a little bit... 

Nope, just some syntactic sugar, not really magic.

(Syntactic sugar: special language features to make an already available pattern easier to write and/or clearer to read for humans)

They are _**VERY**_ abstract, though...

Notes
-----
- "callables lightning talk" refresher
    - what are "callables"?  why make up words?
    - "snippets of code"
        - functions, lambdas
        - callables-calling-callables
    - "code + data"
        - objects, callable objects
    - "code _as_ data"
        - callbacks, helpers
        - closures

- retry with manual syntax
    - simple retry function, hardcoded 3 times
    - retry wrapper, returns new callable
    - we accedentally a decorator

- retry decorator
    - simple decorator, still hardcoded count
        - compare syntax, point to the sugar
    - decorator with count argument
        - wait, if it gets passed the original automatically, where do the args go??
        - callable returning a _decorator_
        - compare syntax, point to the sugar

- "nesting"
    - wrap(X) decorator
    - show manual syntax
    - wrap vs. retry

- other uses of decorators
    - "registering" callables
        - often returns original
    - implementation swap
        - avoid re-checking invariant condition

- what's up with this syntax??


- uses of decorators
    - change the behavior of a callable (e.g. retry, lru_cache)
    - change the behavior of _something else_ "during" a callable
    - register a callable for something
    - implementation swap
    - Frankenstein's monster (e.g. click)

---
