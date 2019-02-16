PySG Comprehensions
===================

(This lesson is presented with [MakeDemo](https://github.com/inventhouse/MakeDemo), which uses a `Makefile` and `code_chunks.py` to drive and organize the examples, please let me know if this makes it hard to follow for anyone else)


### What are they?
- Compact notation for creating a new list (and other collections we'll get to) from another <s>list</s> iterable - [Documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- Four parts (one optional): `new_list = [ expression for-in-iterable (if-check) ]`
    - A new resulting list
    - An expression that can transform each item in the context of the loop and conditional
    - A for-loop over an existing iterable
    - An optional filtering `if`, item and transform are skipped if this is false-ish
- Expression up-front instead of at the end, as it would be in a "normal" for-loop: `for-in-iterable: (if-check:) new_list.append(expression)`
- If-check can be left off; no `else` clause, run `expression` or don't
- Always creates a new list, always iterates over all the items - _not_ "lazy" (but there _is_ a lazy version we'll get to)
- Like `map()` and `filter()` combined

> See `basic_lc`, `basic_for`, and `basic_map_filter` examples in code_chunks.py


### Getting tricky
- Unpacking tuples in iteration works (e.g. `enumerate`)
- Creating tuples (or other objects) is a transform
- Conditional-expression is a transform: `s = str(x) if x else ""`
- Slice-assignment for "in-place" changes: `foo[:] = ["new", "list"]`

> See `tuple_lc`, `tuple_for`, `new_tuple_lc`, `two_kinds_of_if`, and `slice_assign_walk` examples


### Nesting
- Nested for matrix / list-of-
  - Comprehensions are expressions, fairly straightforward
- Doubled is weirder
  - Remember order is just like writing nested loops, still just one expression
  - Used for flattening or combinations
- Can be a short road to spaghetti-town, consider encapsulating inner or using for-loop for outer

> See `matrix_lc`, `combinations_lc`, and `combinations_for` examples


### Other types
- Set - just use curlies: `{ i for i in items }`
- Dict - just use curlies and key: value: `{ k: v for (k, v) in zip(keys, values) }`

> See `set_comp` and `dict_comp` examples


### Generator expressions
- Basic generator - just use parens: `( i for i in items )`
  - Generator produces each line as-needed
- Search Shakespeare
  - Generators working incrementally save memory even if they have to do just as much work!

> See `basic_genex`, `basic_gen_equiv`, `word_search_lc`, and `word_search_gen` examples


### Good code
- Don't use comprehensions when a for-loop is better
  - when you need iteration but not the resulting list
  - when you want to short-circuit (arguably my word search example would be better with a for-loop instead of islice)
  - Consider combining for and comprehension instead of nesting
  - When logic is long or complex, _**BUT...**_
- On the other hand they can encourage _good_ code
  - encapsulate transform and/or condition to make code clearer and simple enough to make a nice comprehension

---
