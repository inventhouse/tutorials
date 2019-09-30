# Example Makefile

default: list  #M Target to run if none is specified

# Requires https://github.com/inventhouse/MakeDemo
# $ path/to/MakeDemo/demoinit
# $ source ./demonow
include $(MakeDemoDir)/MakeDemo.make
ChunkFile := "README.md"

devstack:  # Clone the edX repos with hub
	hub clone edx/devstack && cat devstack/repo.sh | sed -e '1,/^repos=(/ d' -e '/)/,$ d' | sed -e 's/ //g' -e 's,https://github.com/,,' -e 's/\.git//' -e 's/^/hub clone /' | sh

##  Overview  ##
Overview:  ## Quick overview
	@echo "Overview:"
	$(AtChunk)

##  Aliases  ##
Pull-modified:  ## Try to pull a repo with local changes
	@echo -n "git pull -r --autostash" | $(QuietCopy)

Aliases:  ## A few points about git aliases
	$(AtChunk)

Favorites:  ## Some of my favorite aliases
	@gitalias | sort | sed -n -e '/lo =/p' -e '/ss =/p' -e '/co =/p' -e '/pra =/p' -e '/rbm =/p' -e '/cm =/p' -e '/cam =/p'

Gitalias-help:  ## Show gitalias help
	gitalias -h

##  Allgit  ##
List-repos:  ## List all the demo repos
	@ls

Many-repos:  ## Issues with many git repos
	@$(ChunkNamed) "Many Repos"

Allgit-pull:  ## Pull all repos with allgit
	allgit - pra

Allgit:  ## A few points about allgit
	$(AtChunk)

Allgit-ss:  ## Short status of modified repos
	allgit -m - ss

Allgit-diff:  ## Diff of modified repos
	allgit -m - diff

##  BranchFlow  ##
Allgit-checkout:  ## Branch modified repos - but don't really
	@echo "allgit -m - co -b bjh/JIRA-123-add-help-to-makefiles^C"

On-branching:  ## A few points about git branches
	@echo "On branching:"
	@$(ChunkNamed) "On branching"

Meet-newb:  ## Print newb help
	newb -h

BranchFlow:  ## Introducing the BranchFlow commands
	$(AtChunk)

##  Tie it all together  ##
BF-aliases:  ## Show the BranchFlow aliases
	@gitalias | sort | sed -n -e '/^sb =/p' -e '/lb =/p' -e '/nb =/p' -e '/gb =/p' -e '/kb =/p' -e '/db =/p'

Allgit-nb:  ## Actually create some branches
	allgit -m - nb JIRA-123-add-help-to-makefiles

Commit:  ## Commit the changes
	allgit -b ahtm - cam "Add help to Makefiles"

Push:  ## Push up changes
	allgit -b ahtm - push

killb:  # Kill the demo branches
	allgit -b ahtm - kb

##  Final thoughts  ##
Final-thoughts:  ## A couple parting thoughts
	@echo "Final thoughts:"
	@$(ChunkNamed) "Final thoughts"

Video:  ## "Let me show you a high-level picture of how git works..."
	@open "https://vimeo.com/146524997#t=1332s"

include sequence.tmp.mk
# # #
