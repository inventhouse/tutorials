PySG Comprehensions
===================

### What is it?
  - Compact notation to create a new list from another list, nay, iterable
  - four parts (one optional): `new_list = [ expression for-in-iterable (if-check) ]`
    - Always creates a new list, always iterates over all the items - _not_ "lazy" (but there _is_ a lazy version we'll get to)

    ```
    trimmed_lines = [ l.strip() for l in lines ]

    trimmed_lines = []
    for l in lines:
      trimmed_lines.append(l.strip())
    ```

    ```
    content = [ l for l in trimmed_lines if l ]

    content = []
    for l in trimmed_lines:
      if l:
        content.append(l)
    ```

- Some more complex examples & tricks
  - list-of-tuples or enumerate()
  - if-expression
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
