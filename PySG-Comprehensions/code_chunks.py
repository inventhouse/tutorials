# Keeping all the examples in a single file makes them easier to read, edit, and keep consistent with one another; MakeDemo will chunk them out for individual demos.

### header
#!/usr/bin/env python3
# Copyright (c) 2019 Benjamin Holt -- MIT License

### basic_lc
with open("Klein.txt", "r") as klein:

    trimmed_lines = [ l.strip() for l in klein ]
    content = [ l for l in trimmed_lines if l ]

    print("\n".join(content))

### basic_for
with open("Klein.txt", "r") as klein:

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

    trimmed_lines = list(map(lambda l: l.strip(), klein))
    content = list(filter(lambda l: l, trimmed_lines))

    print("\n".join(content))

### Trickier ###
### tuple_lc
with open("Klein.txt", "r") as klein:

    numbered_lines = [ f"{num:3d}: {line}" for (num, line) in enumerate(klein) ]  # Parens optional

    print("".join(numbered_lines))

### tuple_for
with open("Klein.txt", "r") as klein:

    numbered_lines = []
    for (num, line) in enumerate(klein):  # Parens optional
        numbered_lines.append(f"{num:3d}: {line}")

    print("".join(numbered_lines))

### new_tuple_lc
menu = ["spam", "eggs", "sausage", "bacon",]
item_lengths = [ (i, len(i)) for i in menu ]  # Parens required

print(item_lengths)

### two_kinds_of_if
# [name, company, number, street, line_two, city, state, zip]
address = [None, "edX", 141, "Portland St.", None, "Cambridge", "MA", "02139",]
address_values = [ str(v) for v in address if v ]  # No 'else'
print(address_values)  # 'Missing' values dropped

address_values = [ str(v) if v else "" for v in address ]  # 'Else' required
print(address_values)  # Empty strings for 'missing' values

### slice_assign
import os, sys
for current, dirs, files in os.walk(sys.argv[1]):
    # dirs[:] = [ d for d in dirs if d != ".git" ]
    print(current)

### Nesting ###
### matrix_lc
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squares = [ [ n**2 for n in row ] for row in matrix ]
print(squares)

### combinations_lc
fruit = ["banana", "apple", "kiwi",]
not_fruit = ["spam", "eggs", "sausage", "bacon",]

pairs = [ f"{n} and {f}" for f in fruit if len(f) > 4 for n in not_fruit if n != "spam" ]
print(pairs)

### combinations_for
fruit = ["banana", "apple", "kiwi",]
not_fruit = ["spam", "eggs", "sausage", "bacon",]

pairs = []
for f in fruit:
    if len(f) > 4:
        for n in not_fruit:
            if n != "spam":
                pairs.append(f"{n} and {f}")
print(pairs)

### Other types ###
### set_comp
menu = ["spam", "spam", "eggs", "spam", "sausage", "spam", "bacon", "spam",]
print(menu)
item_set = { i for i in menu }  # Just use curlies
print(item_set)

### dict_comp
menu = ["spam", "eggs", "sausage", "bacon",]
item_lengths = { i: len(i) for i in menu }  # Curlies and key: value
print(item_lengths)

### Generators ###
### basic_genex
with open("Klein.txt", "r") as klein:

    trimmed_lines = ( l.strip() for l in klein )  # Parens instead of brackets
    content = ( l for l in trimmed_lines if l )

    print("\n".join(content))

### basic_gen_equiv
with open("Klein.txt", "r") as klein:

    def trimmed_lines():
        for l in klein:
          yield l.strip()

    def content():
        for l in trimmed_lines():
          if l:
            yield l

    print("\n".join(content()))

### word_search_lc
import re, sys
with open(sys.argv[1], "r") as search_file:
    numbered_lines = [ f"{num:6d}: {line}" for (num, line) in enumerate(search_file) ]
    matches = [ l for l in numbered_lines if re.search(sys.argv[2], l, re.IGNORECASE) ]
    match_n = int(sys.argv[3])
    print("".join(matches[:match_n]))

### word_search_gen
from itertools import islice
import re, sys
with open(sys.argv[1], "r") as search_file:
    numbered_lines = ( f"{num:6d}: {line}" for (num, line) in enumerate(search_file) )
    matches = ( l for l in numbered_lines if re.search(sys.argv[2], l, re.IGNORECASE) )
    match_n = int(sys.argv[3])
    print("".join(islice(matches, match_n)))


#####
