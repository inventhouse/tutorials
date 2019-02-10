
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

### tuple_lc
with open("Klein.txt", "r") as klein:

    numbered_lines = [ f"{num:3d}: {line}" for (num, line) in enumerate(klein) ]

    print("\n".join(numbered_lines))

#####
