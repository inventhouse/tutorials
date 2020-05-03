Allgit Tutorial
===============
For many developers, working with lots of repositories while git itself only works on one-at-a-time is a hassle; `allgit` offers flexible automation to fill that gap.

- working with different, sometimes overlapping, groups of repositories
- keeping everything up-to-date
- creating branches consistently
- keeping everything on the right branches
- making changes across multiple repos
- getting all the right repos on a new machine

- project-based scripts and makefiles
- personal scripts
- git submodules & "super-repos"
- `repo` tool
(tedious to maintain or even use, often inflexible, often only covers one project's repos, widely varied from one project or engineer to another, often address only one or a few of the issues above)


Primer
------

| ag & options | sep | command & options |
|--------------|-----|-------------------|
| `allgit`     |`--` | `git status -s`
| Shorthand for git commands:
| `allgit`     | `-` | `status -s`

Demo
----
```
$ ag - pull
(some repos have changes)
$ ag -m - checkout -b my_feature
$ ag -b my_feature - commit -m "WIP my feature"
$ ag -b my_feature - checkout master
$ ag -cb my_feature - rebase master

$ ag -cb master open_release/Ironwood.master my_feature
```


---
