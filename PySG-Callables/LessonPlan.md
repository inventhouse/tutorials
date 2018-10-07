Callables Lesson Plan
=====================
__What is this talk about?__
- Python has many ways to package and refer to standard and custom functionality; ie "code"
- Grazing overview from some of the most fundamental to more esoteric
- Starting very basic but deceptively powerful
- NOT deep into function syntax, scopes, nor calling details

__What the heck are callables?__
- "A callable is anything that can be called" -- [top SO answer](https://stackoverflow.com/questions/111234/what-is-a-callable-in-python#111255); true, but not very helpful
- Why "callable"?  Too many distinct kinds; "function" has baggage

__Snippets of code__
- Functions
- Can call other callables
- Inner functions (basic intro, come back to closure magic shortly)

__Code + data__
- Classes -- `__init__` is like a function
- Methods
- `__call__`
- Generators
- Closures

__Code as data__
- All callables (like everything in Python) are objects that can be:
    - Stored and retrieved
    - Passed and returned
    - Replaced
- bound methods
- lambda?


Menagerie:
----------
- Functions (user-defined, “free functions”)
- Built-in functions (C wrappers)
- Inner functions (closures)
- Lambdas
- Methods
- Bound methods
- Classes (`__new__`, `__init__`)
- Callable objects (`__call__`)
- “Magic methods” (`__dunder__`)
- Generators (yield)
- Coroutines (async)


Example ideas:
--------------
- Text adventure
- Decoder ring
    - [RC4](https://en.wikipedia.org/wiki/RC4)
    - [CipherSaber](http://ciphersaber.gurus.org)
    - [What's the deal with RC4?](https://blog.cryptographyengineering.com/2011/12/15/whats-deal-with-rc4/)
- Runloop
- State machine

---
