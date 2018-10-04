Callables Lesson Plan
=====================

__What the heck are callables?__
- "Things you can call" -- top SO answer; true, but not helpful
- Why "callable"?  "Function" has baggage; too many distinct kinds

__Snippets of code__
- Functions
- Can call other callables
- Inner functions  (basic intro, come back to closure magic shortly)
- Classes -- \__init__ is like a function

__Code + data__
- Methods
- \__call__
- Generators
- Closures

__Code as data__
- All callables (like everything in Python) are objects
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
- Classes (\__new__, \__init__)
- Callable objects (\__call__)
- “Magic methods” (\__dunder__)
- Generators (yield)
- Coroutines (async)


Example ideas:
--------------
- Text adventure
- Decoder ring
- Runloop

---
