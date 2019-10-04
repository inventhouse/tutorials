My Git Workflow Lightning Talk
==============================
_(This presentation is built with MakeDemo, but because it requires other repos, it would be tricky to describe how to set it up to run, sorry; I'll try to make this README cover most of the content, though)_

### Overview
- Many workflows, many tools, just a taste of a few of mine
- Customizing git with aliases
- Working on many repos with allgit
- Streamline branches with BranchFlow

#### Make git work better
To have git just pull changes even if there are local commits or modifications (which is how I *want* `pull` to work) I'd have to type `git pull -r --autostash`; aliases let me shorten that to `git pra`

### Aliases
- Customize git:
    - Shorten common commands
    - Create your own commands
    - Make it work (more) the way *you* want
- A bit arcane though, support is lacking
- `gitalias` for listing, reproducing, and help

#### Favorites
- cam = 'commit -am'
- cm = 'commit -m'
- co = 'checkout'
- lo = 'log -n 10 --oneline'
- pra = 'pull -r --autostash'
- rbm = 'rebase origin/master'
- ss = 'status -s'

#### Gitalias
```
usage: gitalias              Prints existing git aliases
       gitalias -s|--script  Prints git aliases as a script for reproducing
                             them in a new environment
       gitalias -h|--help    Print this message and exit

Create a new alias with:
  git config --global alias.THING 'COMMAND'

Remove an alias with:
  git config --global --unset alias.THING
```

### Many Repos
- One repo per project - but poor support for multiple repos
- Keeping them in sync, making cross-project changes
- Scripts with lists of projects
    - Keeping lists current - more maintenence
    - Not flexible, different sets of repos for different teams
    - Different groups of repos - multiple scripts? Ugh.

### Allgit
- Makes working with many repos easy
- No configuration to add repos
- Run any git command, including aliases
- Platform for other scripts
- Easily filter repos with `-m`, `-b`, or just specifying them
- ...and much more

#### Common allgit commands
- `allgit - pra`
- `allgit -m - ss`
- `allgit -b ahtm - push`
- `allgit -cb master - pra`

### On branching
- Long names are good for shared repos, but terrible for local workflow
    - `zsh` completion helps, but still not great
- Git allows different local vs. remote branch names
    - Arcane to set up

### BranchFlow
- `newb`, `getb`, `setupb` (`nb`, `gb`, `sb`)
    - Long remote branch, automatic short local branch
- `listb` (`lb`)
    - List current and "working" branches
- `dropb`, `killb` (`db`, `kb`)
    - Clean up branches
- Bring it all together with aliases and `allgit`

#### BranchFlow aliases
- db = '! dropb'
- gb = '! getb'
- kb = '! killb'
- lb = '! listb'
- nb = '! newb'
- sb = '! setupb'

### Final thoughts
- All these things can be used independently
- Customize your workflow to *you*

### Links
- [inventhouse/allgit](https://github.com/inventhouse/allgit) - Repository for all these git tools
- [Let me show you a high-level picture of how git works...](https://vimeo.com/146524997#t=1207s) - James Mickens ranting about git

### Outline
- overview
- autostash is awkward
- aliases - customize git
- favorite aliases
- gitalias - so I wrote a tool
    - gitalias -s
- many repos
    - ls
- allgit - pra - so I wrote a tool
- allgit -m - ss
- allgit -m - co -b bjh/JIRA-123-add-help-to-makefiles
    - ugh, so long, switching branches is a pain
    - so I wrote some tools...
    - ...and aliased them
- newb / nb
    - allgit -m - nb bjh/JIRA-123-add-help-to-makefiles
    - commit and push like normal
    - use short branch name
- listb / lb
