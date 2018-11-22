jq Lesson Plan
==============
__What is jq?__
- "[sed](https://en.wikipedia.org/wiki/Sed) for json" - more like "[Cuisinart](https://en.wikipedia.org/wiki/Cuisinart) for json"
- Series of filters
- Filters: Inputs —> Magic —> Outputs

__Simple (but useful!) examples__
- . .foo .[] (and .[].foo)
- Length - it's a filter!

__More filter-like__
- [:] select() test() min_by() max_by()
- Sort_by(), Group_by()

__Munging__
- Boxing / unboxing
- Cleanup / del()

__Advanced__
- Variables and functions
- Errors
- Gotchas


To Do
-----
- Concrete examples
  - Public data source?

---
