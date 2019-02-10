PySG Comprehensions
===================

(This lesson is presented with [MakeDemo](https://github.com/inventhouse/MakeDemo), which uses a `Makefile` and `code_chunks.py` to drive and organize the examples, please let me know if this makes it hard to follow for anyone else)

### What are they?
- Compact notation to create a new list from another <s>list</s> iterable - [PEP 202](https://www.python.org/dev/peps/pep-0202/)
- Four parts (one optional): `new_list = [ expression for-in-iterable (if-check) ]`
- Expression up-front instead of at the end: `for-in-iterable: (if-check:) new_list.append(expression)`
- If-check is optional and can be left off; no `else` clause, run `expression` or don't
- Always creates a new list, always iterates over all the items - _not_ "lazy" (but there _is_ a lazy version we'll get to)
- Like `map()` and `filter()` combined
> See code_chunks.py `basic_lc`, `basic_for`, and `basic_map_filter` examples

### Getting tricky
- Some more complex examples & tricks
  - List-of-tuples or enumerate()
  - Conditional-expression
    ```
    s = str(x) if x else ""  # "Conditional expression", requires `else`

    strings = [ str(i) if i else "" for i in items ]

    strings = []
    for i in items:
      strings.append(str(i) if i else "")
    ```

  - slice-assignment for "in-place" changes
    ```
    import os, sys
    for current, dirs, files in os.walk(sys.argv[1]):
        dirs[:] = [ d for d in dirs if d != ".git" ]
        print(current)
    ```
  - nested

  - anatomy of the double-comprehension
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

- Some overly-complex examples (horrorshow vs. better way, when to use for loops)
  - _(( mine the examples page ))_

- Some ways they can encourage good code
  - encapsulate transform and/or condition to make code clearer and simple enough

- Other types
  - Set
  - Dict
  - Generator - reference Cale's all-hands talk


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
