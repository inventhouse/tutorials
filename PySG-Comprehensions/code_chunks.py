# Keeping all the examples in a single file makes them easier to read, edit, and keep consistent with one another; MakeDemo will chunk them out for individual demos.

### header
#!/usr/bin/env python3
# Copyright (c) 2019 Benjamin Holt -- MIT License

### basic_for
with open("Klein.txt", "r") as klein:

    # "Spelled-out" is less dense, but more flexible (can use 'continue', 'break', 'else', etc)
    trimmed_lines = []
    for line in klein:
        trimmed_lines.append( line.strip() )

    content = []
    for line in trimmed_lines:
        if line:
            content.append( line )

    print("\n".join(content))

### basic_lc
with open("Klein.txt", "r") as klein:

    # List-like brackets, with transform, iteration, and filtering to produce a new result
    trimmed_lines = [ line.strip() for line in klein ]

    content = [ line for line in trimmed_lines if line ]

    print("\n".join(content))

### basic_map_filter
with open("Klein.txt", "r") as klein:

    # Yet another version, here the "expression" part is also near the begininning
    # 'map' runs a callable on each item in an iterable, similar to a comprehension, but have to wrap the expression in 'lambda'
    trimmed_lines = list(map(lambda line: line.strip(), klein))
    # 'filter' runs a callable to include-or-not each item, but doesn't transform them
    content = list(filter(lambda line: line, trimmed_lines))

    print("\n".join(content))

### Trickier ###
### tuple_for
with open("Klein.txt", "r") as klein:

    numbered_lines = []
    # for nl in enumerate(klein):
    #     numbered_lines.append( f"{nl[0]}: {nl[1]}" )  # Ick!

    # Parens optional below
    for (num, line) in enumerate(klein):
        numbered_lines.append( f"{num}: {line}" )

    print("".join(numbered_lines))

### tuple_lc
with open("Klein.txt", "r") as klein:

    # Iteration can unpack tuples and use the parts as usual, here building them into a "format string"
    # Parens optional below
    numbered_lines = [
        f"{num}: {line}"
        for (num, line) in enumerate(klein)
        ]

    print("".join(numbered_lines))

### new_tuple_for
from pprint import pprint  # Pretty-print

# Can create list-of-tuples, or list-of-lists, or list-of-whatever
menu = ["spam", "eggs", "sausage", "bacon",]

item_lengths = []
for i in menu:
    item_lengths.append( (i, len(i)) )

pprint(item_lengths)

### new_tuple_lc
from pprint import pprint  # Pretty-print

# Can create list-of-tuples, or list-of-lists, or list-of-whatever
menu = ["spam", "eggs", "sausage", "bacon",]

item_lengths = [ (i, len(i)) for i in menu ]  # Parens required

pprint(item_lengths)

### two_kinds_of_if_for
from pprint import pprint  # Pretty-print

address = [
    None,
    "edX",
    141,
    "Portland St.",
    None,
    "Cambridge",
    "MA",
    "02139",
    ]

address_drop_missing = []
for v in address:
    if v:  # Filter
        address_drop_missing.append( str(v) )
    # No 'else', just skip

# 'Missing' values dropped
pprint(address_drop_missing)

address_empty_string = []
for v in address:
    address_empty_string.append( str(v) if v else "" )  # 'else' required

# Empty strings for 'missing' values
pprint(address_empty_string)

### two_kinds_of_if_lc
from pprint import pprint  # Pretty-print

address = [
    None,
    "edX",
    141,
    "Portland St.",
    None,
    "Cambridge",
    "MA",
    "02139",
    ]

address_drop_missing = [
    str(v)
    for v in address
    if v  # Filter, no 'else' allowed
    ]

# 'Missing' values dropped
pprint(address_drop_missing)

# "Conditional expression" is just another kind of expression, another type of transform
address_empty_string = [
    str(v) if v else "" # Transform, else required
    for v in address
    ]

# Empty strings for 'missing' values
pprint(address_empty_string)

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
from pprint import pprint  # Pretty-print

# A comprehension _is_ a transform, working on each item (sub-list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]
squares = [
    [ n**2 for n in row ]
    for row in matrix
    ]
pprint(squares)

### combinations_for
from pprint import pprint  # Pretty-print

fruit = ["banana", "apple", "kiwi",]
not_fruit = ["spam", "eggs", "sausage", "bacon",]

pairings = []
for f in fruit:
    if len(f) > 4:
        for n in not_fruit:
            if n != "spam":
                pairings.append( f"{f} and {n}" )

# Pairings lists all combinations of fruits more than 4 letters long and not-fruits except spam
pprint(pairings)

### combinations_lc
from pprint import pprint  # Pretty-print

fruit = ["banana", "apple", "kiwi",]
not_fruit = ["spam", "eggs", "sausage", "bacon",]

# Comprehensions can "nest" like for-loops to produce a single resulting list; one transform with multiple for-if
# Other than expression up-front, order is exactly like nested for-if
pairings = [
    f"{f} and {n}"
    for f in fruit if len(f) > 4
    for n in not_fruit if n != "spam"
    ]
pprint(pairings)

### Other types ###
### set_comp
from pprint import pprint  # Pretty-print

menu = ["spam", "Spam", "EGGS", "sPaM", "sausage", "spaM", "bacon", "sPam",]

item_set = { i.lower() for i in menu }  # Just use curlies

# Only one of each, order is _not_ preserved
pprint(item_set)

### dict_comp
from pprint import pprint  # Pretty-print

menu = ["spam", "eggs", "sausage", "bacon",]

# Curlies and key: value - either/both can be computed
item_lengths = { i.upper(): len(i) for i in menu }

pprint(item_lengths)

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
numbered_lines = [
    f"{n}  {l}"
    for (n, l) in enumerate(lines)
    ]

for l in numbered_lines:
    print(l)

# Reset back to original lines list
del numbered_lines, l

# Produces each line as-needed, no second copy of all the lines!
numbered_lines = (
    f"{n}  {l}"
    for (n, l) in enumerate(lines)
    )

for l in numbered_lines:
    print(l)

### basic_genex
with open("Klein.txt", "r") as klein:

    # Parens instead of brackets
    trimmed_lines = ( l.strip() for l in klein )
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
(file, word, limit) = (sys.argv[1], sys.argv[2], int(sys.argv[3]))
with open(file, "r") as search_file:
    # Produces a list numbering _every_ line of the file, even if we never need them
    numbered_lines = [
        f"{num:6d}: {line}"
        for (num, line) in enumerate(search_file)
        ]

    # Produces a list of every match, even if we don't need them all
    matches = [
        l for l in numbered_lines
        if re.search(word, l, re.IGNORECASE)
        ]

    print("".join(matches[:limit]))

### word_search_gen
from itertools import islice  # Generators are not lists, sometimes need other changes to acommodate
import re, sys
(file, word, limit) = (sys.argv[1], sys.argv[2], int(sys.argv[3]))
with open(file, "r") as search_file:
    # Produces numbered lines as-needed
    numbered_lines = (
        f"{num:6d}: {line}"
        for (num, line) in enumerate(search_file)
        )

    # Finds each match when requested
    matches = (
        l for l in numbered_lines
        if re.search(word, l, re.IGNORECASE)
        )

    # Generators are not natively sliceable, 'islice' does limited iteration
    print("".join(islice(matches, limit)))

#####
