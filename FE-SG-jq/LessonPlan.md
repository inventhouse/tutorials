jq Lesson Plan
==============

Introduction
------------
- What is jq?  Command-line tool for manipulating json; "[sed] for json" - more like "[Cuisinart] for json"
- What is this talk?  Overview of jq starting with some quick easy things that you can start using right away and a glimpse of its depth
- Brief aside on Zipkin and the example data:
  - Distributed process tracing, integrated with Gatsby site compiler used by Prospectus
  - "Trace" is a tree of "spans" with name, timestamp, duration, etc.
  - Web based viewer; Safari handles large traces *much* better than Chrome
  - Save to json; one flat array of span objects, we'll ignore tree / "parentId" here
- The good, jq is:
  - Already written - install with brew / apt-get / standalone binaries available
  - Fast
  - Powerful
  - Variants / conversion tools available for other formats
- The bad, jq is:
  - Kinda complicated
  - Errors can be obtuse
- jq program is a series of filters
- Filters: Inputs —> Magic —> Outputs
- Typical command goes:
  - cat/curl | jq [opts] 'jq program'
  - You can pass the json file to jq instead of piping, but program at the end is easier to edit
  - Single-quotes avoid shell escaping issues
  - Don't confuse the pipes in the jq program for shell pipes


Demos
-----
The demo commands, along with brief notes, are organized in the Makefile; `make list` will print the demo targets.  Some demos will also push their command onto the pasteboard when run.  There is a set of sequential aliases that allow the demos to be run in order by repeatedly sourcing (not just running) the `makenext` script.

### Simple (but useful!) examples
(make 1-6)
- . .foo
- length - it's a filter!

### Munging
(make 7-12)
- .[] and .[].foo
- Slicing
- Unboxing and re-boxing with [ .[] | ]
- Creating dictionaries with {}
- Cleanup fields with del()

### More filter-like
(make 13-17)
- max_by(), select(), test()
- sort_by(), Group_by()

### Advanced
(make 18-21)
- Variables and functions
- Put it all together

### Gotchas & errors
(make 22-26)
- Gotchas
  - Filters run per-input-item unless you -s slurp
  - .[] can unwrap objects
- Common errors:
  - Forgot the dot: "jq: error: name/0 is not defined at <top-level>, line 1:"
  - Need to unwrap array: "jq: error (at <stdin>:1): Cannot index array with string "name""
  - Errors often implicate unix quoting, but rarely is that the issue


Recap
-----
- Pipe data from wherever into jq
- single-quote filter programs
- Pretty-print with '.'
- 'length', 'max_by()', 'min_by()', 'sort_by()', 'group_by()', .[A:B] all work with arrays
- Iterate arrays with '.[]', box into arrays with [ ] or jq -s
- Build objects with '{}', pare them down with 'del()'
- Narrow down with select()
- Explore your data!  Try things!  Write scripts and reports and...


Links
-----
- [jq Manual](https://stedolan.github.io/jq/manual/)
- [Zipkin distributed tracing system](https://zipkin.io)
- [Introduction to sed](http://www.grymoire.com/unix/Sed.html)

[sed]: https://en.wikipedia.org/wiki/Sed
[Cuisinart]: https://en.wikipedia.org/wiki/Cuisinart

---
