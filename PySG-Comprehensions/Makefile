# PySG Comprehensions Makefile
# Copyright (c) 2019 Benjamin Holt -- MIT License

default: list  #M Target to run if none is specified

# Requires https://github.com/inventhouse/MakeDemo
# $ source ./demonow

include $(MakeDemoDir)/MakeDemo.make
ChunkFile := "code_chunks.py"
EDITOR := cat

## Basics ##
intro:  ## Open the README with the lesson outline
	@$(EDITOR) README.md

show_klein:  ## Show the lines we'll be working with
	cat Klein.txt

basic_lc:  ## Create and open basic listcomp example
	@$(ChunkNamed) header > "$@.tmp.py"
	@$(AtChunk) >> "$@.tmp.py"
	@chmod a+x "$@.tmp.py"
	@$(EDITOR) "$@.tmp.py"

run_basic_lc:  ## Run the basic listcomp example
	./basic_lc.tmp.py

basic_for:  ## Create and open equivalent basic for-loop example
	@$(ChunkNamed) header > "$@.tmp.py"
	@$(AtChunk) >> "$@.tmp.py"
	@chmod a+x "$@.tmp.py"
	@$(EDITOR) "$@.tmp.py"

run_basic_for:  ## Run the equivalent basic for-loop example
	./basic_for.tmp.py

basic_map_filter:  ## Create and open equivalent basic for-loop example
	@$(ChunkNamed) header > "$@.tmp.py"
	@$(AtChunk) >> "$@.tmp.py"
	@chmod a+x "$@.tmp.py"
	@$(EDITOR) "$@.tmp.py"

run_basic_map_filter:  ## Run the equivalent basic for-loop example
	./basic_map_filter.tmp.py

## Trickier ##

# # #
clean:  #M Delete the .tmp.py files
	rm *.tmp.py

include sequence.tmp.mk
# # #
