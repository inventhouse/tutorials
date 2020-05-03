Statemachine Line EDitor
========================

To start with, we can just use the default `start` state to manage a few formatting or filtering rules.  For example, we could write a rule like this:

> In the "start" state, if a line matches "Failed: ", remain in the "start" state, and output the line formatted red.

`sled` uses a simple shorthand for adding a rule like this to the state machine, a (non-whitespace) delimiter character of our choice follwed by 7 fields:

> `:state:test:arg:dst:action:arg:tag`

In this case, `state` is "start", of course, the test is `M` for match followed by the pattern; since this pattern includes a `:`, we'll have to choose another delimiter for this rule. `dst` ("destination state") could also be "start", but if we leave it empty the state machine will stay in the same state without having to spell it out.  Finally, we want the action to `F`ormat the output, and we use Python's formatting syntax and the built-in `s`tyle and `i`nput placeholders.  We can also `tag` it with a name; it ends up looking like this:

> `/start/M/Failed: /F/{s.red}{i}{s.off}/FailLine`

Note that this test uses `re.match`, so this rule applies to lines that _start with_ "Failed: ", matching case too.

But what should the machine do with other lines?  Right now, it has no rule for any other input.  Perhaps it makes sense to just pass all other input unchanged.  The most convenient way to do that is simply the `-p` flag, but let's go ahead and write the rule for it.

We could connect this rule to the "start" state but, kinda like leaving out the `dst`, not specifying a `state` adds the rule to all states to be tested after any explicit rules.  We don't need to match anything, we can just use the `T`rue test, which doesn't take an argument, and again we'll omit `dst`.  Passing the input is common enough there's an action, `I`, for that; it doesn't take an argument.  Again, we'll `tag` it with a name:

> `::T:::I::PassAll`


