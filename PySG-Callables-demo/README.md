Callables Lesson Plan
=====================

### Intro
What is this talk about?
- Python has many ways to package and refer to standard and custom functionality; ie "code"
- Grazing overview from some of the most fundamental to more esoteric
- Starting very basic but deceptively powerful
- NOT deep into function syntax, scopes, nor calling details


### Callables
What the heck are "callables"?
- "A callable is anything that can be called" -- [top StackOverflow answer][1]; true, but not very helpful
- Why "callable"?  Too many distinct kinds; the term "function" has baggage

[1]: https://stackoverflow.com/questions/111234/what-is-a-callable-in-python#111255


### Snippets
Basically, callables are snippets of code
- Functions
- Can call other callables
- Inner functions (basic intro, come back to closure magic shortly)

#### Demo
- caesar_function


### Code with data
Combining code with data is very powerful, Python has several ways to do that
- Classes -- `__init__` is like a function
- Methods
- `__call__`
- Generators
- Closures

#### Demo
- caesar_class
- fibonacci_gen
- caesar_closure


### Code as data
- All callables (like everything in Python) are objects that can be:
    - Stored and retrieved
    - Passed and returned
    - Replaced
- bound methods can be passed like functions

#### Demo
- caesar_bound
- Vigenère


Menagerie
---------
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


Links
-----
- [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number)
- [Lehmer RNG](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
- [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

---
