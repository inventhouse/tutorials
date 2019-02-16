# Keeping all the examples in a single file makes them easier to read, edit, and keep consistent with one another; MakeDemo will chunk them out for individual demos.

### header
#!/usr/bin/env python3
# Copyright (c) 2019 Benjamin Holt -- MIT License

### basic_lc
with open("Klein.txt", "r") as klein:

    # List-like brackets, with transform, iteration, and filtering to produce a new result
    trimmed_lines = [ l.strip() for l in klein ]
    content = [ l for l in trimmed_lines if l ]

    print("\n".join(content))

### basic_for
with open("Klein.txt", "r") as klein:

    # "Spelled-out" is less dense, but more flexible (can use 'continue', 'break', 'else', etc)
    trimmed_lines = []
    for l in klein:
      trimmed_lines.append(l.strip())

    content = []
    for l in trimmed_lines:
      if l:
        content.append(l)

    print("\n".join(content))

### basic_map_filter
with open("Klein.txt", "r") as klein:

    # Yet another version, here the "expression" part is also near the begininning
    # 'map' runs a callable on each item in an iterable, similar to a comprehension, but have to wrap the expression in 'lambda'
    trimmed_lines = list(map(lambda l: l.strip(), klein))
    # 'filter' runs a callable to include-or-not each item, but doesn't transform them
    content = list(filter(lambda l: l, trimmed_lines))

    print("\n".join(content))

### Trickier ###
### tuple_lc
with open("Klein.txt", "r") as klein:

    # Iteration can unpack tuples and use the parts as usual, here building them into a "format string"
    numbered_lines = [ f"{num:3d}: {line}" for (num, line) in enumerate(klein) ]  # Parens optional

    print("".join(numbered_lines))

### tuple_for
with open("Klein.txt", "r") as klein:

    numbered_lines = []
    for (num, line) in enumerate(klein):  # Parens optional
        numbered_lines.append(f"{num:3d}: {line}")

    print("".join(numbered_lines))

### new_tuple_lc
# Can create list-of-tuples, or list-of-lists, or list-of-whatever
menu = ["spam", "eggs", "sausage", "bacon",]
item_lengths = [ (i, len(i)) for i in menu ]  # Parens required

print(item_lengths)

### two_kinds_of_if
# "Conditional expression" is just another kind of expression, another type of transform
# [name, company, number, street, line_two, city, state, zip]
address = [None, "edX", 141, "Portland St.", None, "Cambridge", "MA", "02139",]

address_values = [ str(v) for v in address if v ]  # Filter, no 'else' allowed
print(address_values)  # 'Missing' values dropped

address_values = [ str(v) if v else "" for v in address ]  # Transform, 'else' _required_
print(address_values)  # Empty strings for 'missing' values

### slice_assign_viz
l = [1,2,3]
l_a = l  # Points to the same list as 'l'
l_a = [4,5,6]  # Now points to a different list; 'l' is unchanged

l_a = l  # Points to the same list as 'l'
l_a[1] = 'a'  # Change an item in that list

l_a[:] = [4,5,6,7,8,9]  # Change *all* the items in that list

### slice_assign_walk
import os, sys
# Modifying 'dirs' in-place controls where os.walk will descend; slice-assignment "copies back in" the new list
for current, dirs, files in os.walk(sys.argv[1]):
    # dirs[:] = [ d for d in dirs if d != ".git" ]  # Uncomment and re-run to not descend into .git directories
    print(current)

### Nesting ###
### matrix_lc
# A comprehension _is_ a transform, working on each item (sub-list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squares = [ [ n**2 for n in row ] for row in matrix ]
print(squares)

### combinations_for
fruit = ["banana", "apple", "kiwi",]
not_fruit = ["spam", "eggs", "sausage", "bacon",]

pairings = []
for f in fruit:
    if len(f) > 4:
        for n in not_fruit:
            if n != "spam":
                pairings.append(f"{n} and {f}")

# Pairings lists all combinations of fruits more than 4 letters long and not-fruits except spam
print(pairings)

### combinations_lc
fruit = ["banana", "apple", "kiwi",]
not_fruit = ["spam", "eggs", "sausage", "bacon",]

# Comprehensions can "nest" like for-loops to produce a single resulting list; one transform with multiple for-if
# Other than expression up-front, order is exactly like nested for-if
pairings = [ f"{n} and {f}" for f in fruit if len(f) > 4 for n in not_fruit if n != "spam" ]
print(pairings)

### Other types ###
### set_comp
menu = ["spam", "spam", "eggs", "spam", "sausage", "spam", "bacon", "spam",]
item_set = { i for i in menu }  # Just use curlies
print(item_set)  # Only one of each, order is _not_ preserved

### dict_comp
menu = ["spam", "eggs", "sausage", "bacon",]
item_lengths = { i: len(i) for i in menu }  # Curlies and key: value
print(item_lengths)

### Generators ###
### genex_viz
lines = [
    "A mathematician named Klein",
    "Thought the Möbius band was divine.",
    "Said he: “If you glue",
    "The edges of two,",
    "You’ll get a weird bottle like mine.”",
    "- Leo Moser",
]

# Brackets here, parens below, that's the _only_ change
numbered_lines = [ f"{n}  {l}" for (n, l) in enumerate(lines) ]

for l in numbered_lines:
    print(l)

del numbered_lines, l

numbered_lines = ( f"{n}  {l}" for (n, l) in enumerate(lines) )
# Produces each line as-needed, no second copy of all the lines!

for l in numbered_lines:
    print(l)

### basic_genex
with open("Klein.txt", "r") as klein:

    trimmed_lines = ( l.strip() for l in klein )  # Parens instead of brackets
    content = ( l for l in trimmed_lines if l )

    print("\n".join(content))

### basic_gen_equiv
with open("Klein.txt", "r") as klein:

    def trimmed_lines():
        for l in klein:
            # 'yield' is like "return with a bookmark", each 'next' resumes running here
            yield l.strip()

    def content():
        for l in trimmed_lines():
          if l:
            yield l

    # 'join' iterates over 'content' which iterates over 'trimmed_lines' which iterates over the open file
    print("\n".join(content()))

### word_search_lc
import re, sys
with open(sys.argv[1], "r") as search_file:
    numbered_lines = [ f"{num:6d}: {line}" for (num, line) in enumerate(search_file) ]  # Produces a list numbering _every_ line of the file, even if we never need them
    matches = [ l for l in numbered_lines if re.search(sys.argv[2], l, re.IGNORECASE) ]  # Produces a list of every match, even if we don't need them all
    match_n = int(sys.argv[3])
    print("".join(matches[:match_n]))

### word_search_gen
from itertools import islice  # Generators are not lists, sometimes need other changes to acommodate
import re, sys
with open(sys.argv[1], "r") as search_file:
    numbered_lines = ( f"{num:6d}: {line}" for (num, line) in enumerate(search_file) )  # Produces numbered lines as-needed
    matches = ( l for l in numbered_lines if re.search(sys.argv[2], l, re.IGNORECASE) )  # Finds each match when requested
    match_n = int(sys.argv[3])
    print("".join(islice(matches, match_n)))  # Generators are not natively sliceable, 'islice' does limited iteration

#####
