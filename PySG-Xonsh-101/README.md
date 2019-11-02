Xonsh 101
=========

Introduction
------------
"If you know Python and you use Bash ever, you already know why you want more Python in your shell." - Aaron Christianson (ninjaaron)

### Shell is great
- Run commands - direct invocation, "builtins", and transparent fallback "path"
    - arguments, flags, subcommands, and other "command line interface"
- Pipelines - link small commands together to do remarkable things
- Customization - helpful prompt, aliases, configurable path
- Scripting

### Shell is terrible
- Everything is strings
- Often parsed badly; problems _everywhere_
    - `"Quotes" won't save you! 🤦‍♂️` is a valid filename
        - "But that's an edge-case" - our jobs would be __*SO*__ easy if we didn't have to deal with edge-cases!
        - Weird filenames exist, like `/bin/[` - see if you can spot that later in this section
- Lots of commands are arcane (and archaic)
- Syntax is insane; I wrote this, don't be like me:
```bash
: ${GetChunkDelim:="###"}
if [ "$1" == "-h" -o "$1" == "--help" -o -z "$1" -o -z "$2" ]; then
  cat <<USAGE
usage:...
USAGE
  exit 0
fi
cat "$1" | sed -e"1,/^${GetChunkDelim}[ 	][ 	]*$2/ d" -e"/^${GetChunkDelim}/,$ d"
```

### Python is great
- Real data structures
- Real control structures
- Lots of powerful libraries
...but not good at shell things (from the `subprocess` docs):
```python
# $ dmesg | grep hda
p1 = Popen(["dmesg"], stdout=PIPE)
p2 = Popen(["grep", "hda"], stdin=p1.stdout, stdout=PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output = p2.communicate()[0]
```

### Why not both?
Imagine an environment with...
- Simple, direct, command invocation, with all your old shell friends
- Pipes, redirection, job control
- Full Python interpreter
- Fancy prompts, completions, extensions
- True multi-line editing

### Unicorn
```
`\
  \\,
   \\\,^,.,,.
   ,;7~((\))`;;,,
   ,(@') ;)`))\;;',
    )  . ),((  ))\;,
   /;`,,/7),)) )) )\,,      ,,,... ,
  (& )`   (,((,((;( ))\,_,,;'`    `\\,
   `"    ` ), ))),/( (            `)\,
          '1/';/;  `               ))),
           (, (     /         )    ((/,
          / \                /     ((('
         ( 6--\%  ,>     ,,,(     /'))\'
          \,\,/ ,/`----~`\   \    >,))))'
            \/ /          `--7>' /((((('
            (,9             // /'('((\\\,
             \ \,,         (/,/   '\`\\'\
              `\_)1        (_)Kk    `\`\\`\
                `\|         \Z          `\
                  `          "            `
```

### Xonsh
- Pronounced like 'K'; spelled with an 'X' 'cos Xes are cool
- Brings together Python and shell (aka "subprocess mode")
- With ways to work with both and move data between the two
- Plus loads of modern terminal bells & whistles, customizability, etc.

### What's it like?
- Mostly "just works" - type shell commands and pipelines or python at any prompt anytime
- Best of both worlds: great shell features, and _WAY_ better than the standard python interpreter
- Configuration takes some learning and experimentation
- Interaction between shell and python _definitely_ takes some learning and experimentation

### Examples

### Gotchas
- Backticks different than sh/bash, use `$()`
- Must use `env` for setting "temporary" env vars
- Tricky to use pipes in aliases
- _Not_ recommended as `$SHELL` - set in terminal apps instead
- Anaconda and some other "activate"-type things expect `sh`-like shells
- Still new; some rough spots, documentation is thin in places - contribute!


Links
-----
- [Talks & articles](https://xon.sh/talks_and_articles.html)
    - Check out the PyCon talk for a whirlwind tour; somewhat dated, xonsh has improved significantly since then, but still impressive and entertaining
- [Xonsh installation](https://xon.sh/#installation)
    - Lots of ways to install, pick your poison `¯\_(ツ)_/¯`
- [Xonsh quickstart](https://github.com/ninjaaron/xonsh-quickstart#basic-configuration-etc)
    - _Really_ good tutorial, maybe better than the official one
    - While you're in the neighborhood, this is also really good:
        - [Replacing Bash Scripting with Python](https://github.com/ninjaaron/replacing-bash-scripting-with-python)
- [Xonsh cheatsheet](https://github.com/xonsh/xonsh/wiki/Cheatsheet)
    - Keep this handy when you're learning the different modes / substitutions / extensions to navigate the choppy waters where Python and Shell mix
- [Official tutorial](https://xon.sh/tutorial.html)
    - Definitely read this and refer to it, but I've found the previous two links more usful "in the moment"
- [Home page](https://xon.sh/)
    - Lots more documentation here, keep diging as you get more familiar or you find you have specific needs
- [Source code](https://github.com/xonsh/xonsh)
    - The great thing about a shell written in the language it's based on is that you can read the code to understand how it really works - and contribute back!
- [Virtualenv discussion](https://github.com/xonsh/xonsh/issues/2663)

Other interesting shells
------------------------
- [Daudin](https://github.com/terrycojones/daudin)
    - Another Python shell, _very_ interesting pipelining system
- [Nushell](http://www.jonathanturner.org/2019/08/introducing-nushell.html)
    - _Fascinating_ "structured data"-based shell, apparently at least in part inspired by...
- [Powershell](https://en.wikipedia.org/wiki/PowerShell)
    - I think I should learn more about this

---
