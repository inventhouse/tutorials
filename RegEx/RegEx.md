RegEx Thoughts
==============

### RegEx Primer / Refresher

_(( the most basic things common to most RE dialects ))_


### Things That Are Confusing In RE Syntax:
- Character classes/sets - the rules are different here (except when they still apply)
- ? means different things in different places
- ^ also has multiple meanings


### Composing:
- Keep RE documentation handy; they're complicated, it's OK to not know all the syntax cold - I still don't
  - Different RE engines have different features / syntax / quirks / etc. anyway
- Consider what you want from the match
  - Just match?
  - Parse out fields?
  - How precise/selective vs. lenient/robust?
- Work from exemplars
  - keep the exemplars as comments with the regex so others can see how they relate
- Edit a copy of a line to develop the RE
- Look for "anchors" - labels, delimiters, etc. that don't change
- Work in chunks, test frequently
- Mind the greed - reluctant operators are (often) good
- Use named groups for capture and self-documentation, don't be shy with groups
- Don't be afraid to use multiple REs
  - State machines of REs are really powerful


### Troubleshooting:
- Run lots of inputs through simple "Match/No Match" script, look for "surprises"
- Compare line that should / shouldn't have matched to exemplars
  - If it unexpectedly didn't match, look for differences
    - Run against subsections of the RE; where does the match "break"?
    - Check for strange characters, whitespace, etc. (`cat -vet`, `hexdump -C`)
  - If it unexpectedly did match, look for overly-greedy clauses / lack of anchors
    - Look at what got captured in each group - add groups if needed
    - Why shouldn't this have matched? (Or: "what should have broken the match?")
    - Remember `*` can match nothing or can slurp up the rest of the input
- Beware of "syntax" characters in the pattern/anchors (eg `.` will match a literal dot - and anything else!)
- Add troublesome lines to exemplars for future reference/testing


### Tips For Robust REs:

_(( write this ))_
- Use built-in classes `\s` etc.


### Worked Example:

_(( write this ))_

```
5a9714e Add note about python versions and anaconda environments
^(?P<sha>[0-9a-fA-F]+)\s+(?P<message>.+)
```

---
