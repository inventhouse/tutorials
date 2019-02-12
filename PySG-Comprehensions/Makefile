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

basic_map_filter:  ## Create and open equivalent basic map-filter example
	@$(ChunkNamed) header > "$@.tmp.py"
	@$(AtChunk) >> "$@.tmp.py"
	@chmod a+x "$@.tmp.py"
	@$(EDITOR) "$@.tmp.py"

run_basic_map_filter:  ## Run the equivalent basic map-filter example
	./basic_map_filter.tmp.py

## Trickier ##
tuple_lc:  ## Create and open comp over tuples example
	@$(ChunkNamed) header > "$@.tmp.py"
	@$(AtChunk) >> "$@.tmp.py"
	@chmod a+x "$@.tmp.py"
	@$(EDITOR) "$@.tmp.py"

run_tuple_lc:  ## Run the comp over tuples example
	./tuple_lc.tmp.py

tuple_for:  # # Create and open equivalent basic loop over tuples example
	@$(ChunkNamed) header > "$@.tmp.py"
	@$(AtChunk) >> "$@.tmp.py"
	@chmod a+x "$@.tmp.py"
	@$(EDITOR) "$@.tmp.py"

run_tuple_for:  # # Run the equivalent basic loop over tuples example
	./tuple_for.tmp.py

new_tuple_lc:  ## Create and open new tuples example
	@$(ChunkNamed) header > "$@.tmp.py"
	@$(AtChunk) >> "$@.tmp.py"
	@chmod a+x "$@.tmp.py"
	@$(EDITOR) "$@.tmp.py"

run_new_tuple_lc:  ## Run the new tuples example
	./new_tuple_lc.tmp.py

two_kinds_of_if:  ## Create and open two kinds of if example
	@$(ChunkNamed) header > "$@.tmp.py"
	@$(AtChunk) >> "$@.tmp.py"
	@chmod a+x "$@.tmp.py"
	@$(EDITOR) "$@.tmp.py"

run_two_kinds_of_if:  ## Run the two kinds of if example
	./two_kinds_of_if.tmp.py

## Generator Expressions ##
Shakespeare.txt:  # Download complete works of shakespeare
	curl -o Shakespeare.txt "https://www.gutenberg.org/files/100/100-0.txt"

word_search_lc:  ## Create and open the list comprehension version of word search
	@$(ChunkNamed) header > "$@.tmp.py"
	@$(AtChunk) >> "$@.tmp.py"
	@chmod a+x "$@.tmp.py"
	@$(EDITOR) "$@.tmp.py"

run_word_search_lc: Shakespeare.txt  ## Run the list comprehension version of word search
	/usr/bin/time -l ./word_search_lc.tmp.py "Shakespeare.txt" "beauty" 10 2>&1 | head -13

word_search_gen:  ## Create and open the generator expression version of word search
	@$(ChunkNamed) header > "$@.tmp.py"
	@$(AtChunk) >> "$@.tmp.py"
	@chmod a+x "$@.tmp.py"
	@$(EDITOR) "$@.tmp.py"

run_word_search_gen: Shakespeare.txt  ## Run the generator expression version of word search
	/usr/bin/time -l ./word_search_gen.tmp.py "Shakespeare.txt" "beauty" 10  2>&1 | head -13

py_hi:  ## Measure Python printing 'hi'
	/usr/bin/time -l python -c "print('hi')" 2>&1 | head -3

echo_hi:  # Measure echo printing 'hi'
	/usr/bin/time -l echo hi 2>&1 | head -3

# # #
clean:  #M Delete the .tmp.py files
	rm *.tmp.py

include sequence.tmp.mk
# # #
