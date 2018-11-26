jq Lesson Plan
==============

What is jq?
-----------
- "[sed] for json" - more like "[Cuisinart] for json"
- Overview of jq starting with the quick easy things that you can start using right away and a glimpse of its depth
- Brief aside on Zipkin and the example data:
  - Distributed process tracing
  - Logical tree of "spans" with name, timestamp, duration, etc.
  - Web based viewer; Safari handles large traces *much* better than Chrome
  - Save to json; one flat array of span objects, we'll ignore tree / "parentId"
- jq program is a series of filters
- Filters: Inputs —> Magic —> Outputs
- The good, jq is:
  - Already written
  - Fast
  - Powerful
  - Variants / conversion tools available for other formats
- The bad, jq is:
  - Kinda complicated
  - Errors can be obtuse


### Simple (but useful!) examples
(make 1-6)
- . .foo
- Length - it's a filter!


### Munging
(make 7-13)
- .[] and .[].foo
- Slicing
- Unboxing and re-boxing with [ .[] | ]
- Creating dictionaries with {}
- Cleanup fields with del()


### More filter-like
(make 14-18)
- max_by(), select(), test()
- Sort_by(), Group_by()


### Advanced
(make 19-27)
- Variables and functions
- Put it all together
- Gotchas
  - Filters run per-input-item unless you -s slurp
- Common errors:
  - Forgot the dot: "jq: error: name/0 is not defined at <top-level>, line 1:"
  - Need to unwrap array: "jq: error (at <stdin>:1): Cannot index array with string "name""
  - Errors often implicate unix quoting, but rarely is


### Recap
- Pretty-print with '.'
- 'length', 'max_by()', 'min_by()', 'sort_by()', 'group_by()', slicing all work with arrays
- Iterate arrays with '.[]', box into arrays with [ ] or jq -s
- Build objects with '{}', pare them down with 'del()'
- Filter with select()


### To Do:
- Basic syntax: curl/cat | jq [opts] ['single-quoted filter'|-f FILTER.jq] [Or input file can go here]
- add recap & recap target
- add (up next) prompts to help with flow
- if possible, work out 'make next'


### Links
- [jq Manual](https://stedolan.github.io/jq/manual/)
- [Zipkin distributed tracing system](https://zipkin.io)
- [Introduction to sed](http://www.grymoire.com/unix/Sed.html)

[sed]: https://en.wikipedia.org/wiki/Sed
[Cuisinart]: https://en.wikipedia.org/wiki/Cuisinart

---
