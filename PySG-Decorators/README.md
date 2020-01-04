
Decorators, how do they work??
==============================
Spoiler: They're **not** magic!

Well, maybe just a little bit... 

Nope, just some syntactic sugar, not really magic.

(Syntactic sugar: special language features to make an already available pattern easier to write and/or clearer to read for humans)

They are _**VERY**_ abstract, though...

Outline
-------
- Callables "lightning talk" refresher
    - what are "callables"?  why make up words?
        - "A callable is anything that can be called" -- [top StackOverflow answer][1]; true, but not very helpful
        - Why "callable"?  Too many distinct kinds; the term "function" has baggage
    - "Snippets of code"
        - Functions, lambdas
        - Easy to take for granted, but very powerful:
            - Can take parameters, return results
            - Callables can call other callables
    - "Code + data"
        - `__init__`, callable objects, bound methods
    - "Code _as_ data"
        - callbacks, helpers
        - closures

[1]: https://stackoverflow.com/questions/111234/what-is-a-callable-in-python#111255


- `retry` with manual syntax
    - Simple `retry` function, hardcoded 3 times
    - `retry` wrapper, returns new callable
    - We accedentally a decorator

- `retry` decorator
    - Simple decorator, still hardcoded count
        - compare syntax, point to the sugar
    - Decorator with count argument
        - Wait, if it gets passed the original automatically, where do the args go??
        - Callable returning a _decorator_
        - Compare syntax, point to the sugar

- "Nesting"
    - Bold vs. italics decorators
    - Show manual syntax

- Professional touches
    - use `*args` and `**kwargs`
    - use `functools.wraps(f)`

- Uses of decorators
    - Change the behavior of a callable (e.g. retry, lru_cache, ddt)
    - Change the behavior of _something else_ "during" a callable

- Other uses of decorators
    - "Registering" callables
        - Often returns original
    - Implementation swap
        - Avoid re-checking invariant condition
    - Frankenstein's monster (e.g. click)

- What's up with this syntax??

---
