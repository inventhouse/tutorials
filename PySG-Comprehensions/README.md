PySG Comprehensions
===================

(This lesson is presented with [MakeDemo](https://github.com/inventhouse/MakeDemo), which uses a `Makefile` and `code_chunks.py` to drive and organize the examples, please let me know if this makes it hard to follow for anyone else)


### What are they?
- Compact notation for creating a new list from another <s>list</s> iterable - [PEP 202](https://www.python.org/dev/peps/pep-0202/)
- Four parts (one optional): `new_list = [ expression for-in-iterable (if-check) ]`
- Expression up-front instead of at the end: `for-in-iterable: (if-check:) new_list.append(expression)`
- If-check is optional and can be left off; no `else` clause, run `expression` or don't
- Always creates a new list, always iterates over all the items - _not_ "lazy" (but there _is_ a lazy version we'll get to)
- Like `map()` and `filter()` combined
> See `basic_lc`, `basic_for`, and `basic_map_filter` examples in code_chunks.py


### Getting tricky
- Unpacking tuples (e.g. `enumerate`)
- Creating tuples
- Conditional-expression
  `s = str(x) if x else ""`
- slice-assignment for "in-place" changes
  `foo[:] = ["new", "list"]`
  - pythontutor to understand this?


### Nesting
- Nested for matrix / list-of-
  - Comprehensions are expressions, fairly straightforward
- Doubled is weirder
  - Remember order is just like writing nested loops, still just one expression
  - Used for flattening or combinations
- Can be a short road to spaghetti-town, consider encapsulating inner or using for-loop for outer
    ```
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [x for l in list_of_lists for x in l]

    flattened = []
    for l in list_of_lists:
        for x in l:
            flattened.append(x)

    flattened = []
    for l in list_of_lists:
        flattened.extend(l)
        # flattened.extend([ str(x) for x in l ])
    ```

- Other types
  - Set
  - Dict

- Generator expressions
  - Basic generator
  - Search Shakespeare


### Good code
- Don't use comprehensions when a for-loop is better
  - when you need iteration but not the resulting list
  - when you want to short-circuit (arguably my word search example would be better with a for-loop instead of islice)
  - Consider combining for and comprehension instead of nesting
  - When logic is long or complex, _**BUT...**_
- On the other hand they can encourage _good_ code
  - encapsulate transform and/or condition to make code clearer and simple enough to make a nice comprehension


Notes and junk
--------------
- formatting: list = [1, 2, 3,] - no bracket padding, comp = [ i for i in list ] - padded brackets

- maybe mention py2 vs py3 scope change for list comprehensions

- if at beginning vs. end - brief refresher on statements & expressions
- double comprehensions
- comprehension in expression places (ex 8 - ex 8 is bad for other reasons)
- nested comprehensions

- generator expressions - people will want to know more about generators

---
