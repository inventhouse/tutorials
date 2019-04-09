# PySG Comprehensions Makefile
# Copyright (c) 2019 Benjamin Holt -- MIT License

default: list  #M Target to run if none is specified

# Requires https://github.com/inventhouse/MakeDemo
# $ source ./demonow

include $(MakeDemoDir)/MakeDemo.make
ChunkFile := "code_chunks.py"
# EDITOR := cat
EDITOR := atom
EditorAt := "$(MakeDemoDir)/atom_at"
ReadFile := "README.md"
ReadAt = $(EditorAt) $(ReadFile)
# ReadChunk = $(GetChunk) "README.md"
Spaces = echo; echo

%.tmp.py:
	@$(ChunkNamed) header > "$@"
	@$(ChunkNamed) "$(@:.tmp.py=)" >> "$@"
	@chmod a+x "$@"

.SECONDEXPANSION:

## Basics ##
intro:  #- Open the README with the lesson outline
	@$(EDITOR) README.md

show_klein:  ## Show the lines we'll be working with
	@open https://en.wikipedia.org/wiki/Klein_bottle
	cat Klein.txt
	@$(Spaces)

show_what:  #- Show the "what are they?" section
	# @$(ReadAt) "### What are they?"
	@open "https://github.com/inventhouse/tutorials/tree/master/PySG-Comprehensions#what-are-they"

basic_for: $$@.tmp.py  ## Create and open equivalent basic for-loop example
	@$(EDITOR) "$<"

run_basic_for: $$(subst run_,,$$@).tmp.py  ## Run the equivalent basic for-loop example
	@$(Spaces)
	"./$<"
	@$(Spaces)

basic_lc: $$@.tmp.py  ## Create and open basic listcomp example
	@$(EDITOR) "$<"

run_basic_lc: $$(subst run_,,$$@).tmp.py  ## Run the basic listcomp example
	@$(Spaces)
	"./$<"
	@$(Spaces)

basic_map_filter: $$@.tmp.py  #- Create and open equivalent basic map-filter example
	@$(EDITOR) "$<"

run_basic_map_filter: $$(subst run_,,$$@).tmp.py  #- Run the equivalent basic map-filter example
	@$(Spaces)
	"./$<"
	@$(Spaces)

## Trickier ##
_getting_tricky_:  ## "Getting Tricky" segue
	@true

show_tricky:  #- Show the "getting tricky" section
	# @$(ReadAt) "### Getting tricky"
	@open "https://github.com/inventhouse/tutorials/tree/master/PySG-Comprehensions#getting-tricky"

tuple_for: $$@.tmp.py  ## Create and open equivalent loop over tuples example
	@$(EDITOR) "$<"

run_tuple_for: $$(subst run_,,$$@).tmp.py  #- Run the equivalent basic loop over tuples example
	@$(Spaces)
	"./$<"
	@$(Spaces)

tuple_lc: $$@.tmp.py  ## Create and open comp over tuples example
	@$(EDITOR) "$<"

run_tuple_lc: $$(subst run_,,$$@).tmp.py  ## Run the comp over tuples example
	@$(Spaces)
	"./$<"
	@$(Spaces)

new_tuple_for: $$@.tmp.py  ## Create and open new tuples for-loop example
	@$(EDITOR) "$<"

new_tuple_lc: $$@.tmp.py  ## Create and open new tuples comp example
	@$(EDITOR) "$<"

run_new_tuple_lc: $$(subst run_,,$$@).tmp.py  ## Run the new tuples example
	@$(Spaces)
	"./$<"
	@$(Spaces)

two_kinds_of_if_for: $$@.tmp.py  ## Create and open two kinds of if spelled-out example
	@$(EDITOR) "$<"

run_two_kinds_of_if_for: $$(subst run_,,$$@).tmp.py  #- Run the two kinds of if spelled-out example
	@$(Spaces)
	"./$<"
	@$(Spaces)

two_kinds_of_if_lc: $$@.tmp.py  ## Create and open two kinds of if example
	@$(EDITOR) "$<"

run_two_kinds_of_if_lc: $$(subst run_,,$$@).tmp.py  ## Run the two kinds of if example
	@$(Spaces)
	"./$<"
	@$(Spaces)

slice_assign_viz:  #- Copy slice-assignment example and open pythontutor.com
	@echo "Copying $@, paste into pythontutor"
	$(AtChunk) | $(QuietCopy)
	open "http://pythontutor.com/visualize.html#mode=edit"

slice_assign_walk: $$@.tmp.py  #- Create and open slice assign example
	@$(EDITOR) "$<"

run_slice_assign_walk: $$(subst run_,,$$@).tmp.py  #- Run the slice assign example
	@$(Spaces)
	"./$<" ..
	@$(Spaces)

## Nesting ##
_nesting_:  ## "Nesting" segue
	@true

show_nesting:  #- Show the "nesting" section
	# @$(ReadAt) "### Nesting"
	@open "https://github.com/inventhouse/tutorials/tree/master/PySG-Comprehensions#nesting"

matrix_lc: $$@.tmp.py  ## Create and open matrix example
	@$(EDITOR) "$<"

run_matrix_lc: $$(subst run_,,$$@).tmp.py  ## Run the matrix example
	@$(Spaces)
	"./$<"
	@$(Spaces)

combinations_for: $$@.tmp.py  ## Create and open combinations loop example
	@$(EDITOR) "$<"

run_combinations_for: $$(subst run_,,$$@).tmp.py  ## Run the combinations loop example
	@$(Spaces)
	"./$<"
	@$(Spaces)

combinations_lc: $$@.tmp.py  ## Create and open combinations listcomp example
	@$(EDITOR) "$<"

run_combinations_lc: $$(subst run_,,$$@).tmp.py  ## Run the combinations listcomp example
	@$(Spaces)
	"./$<"
	@$(Spaces)

## Other Types ##
_other_types_:  ## "Other Types" segue
	@true

show_other:  #- Show the "other types" section
	# @$(ReadAt) "### Other types"
	@open "https://github.com/inventhouse/tutorials/tree/master/PySG-Comprehensions#other-types"

set_comp: $$@.tmp.py  ## Create and open set comprehension example
	@$(EDITOR) "$<"

run_set_comp: $$(subst run_,,$$@).tmp.py  ## Run the set comprehension example
	@$(Spaces)
	"./$<"
	@$(Spaces)

dict_comp: $$@.tmp.py  ## Create and open dict comprehension example
	@$(EDITOR) "$<"

run_dict_comp: $$(subst run_,,$$@).tmp.py  ## Run the dict comprehension example
	@$(Spaces)
	"./$<"
	@$(Spaces)

## Generator Expressions ##
_gen_expressions_:  ## "Generator Expressions" segue
	@true

show_gen:  #- Show the "generator expressions" section
	# @$(ReadAt) "### Generator expressions"
	@open "https://github.com/inventhouse/tutorials/tree/master/PySG-Comprehensions#generator-expressions"

genex_viz:  ## Copy generator expression example and open pythontutor.com
	@echo "Copying $@, paste into pythontutor"
	$(AtChunk) | $(QuietCopy)
	open "http://pythontutor.com/visualize.html#mode=edit"

basic_genex: $$@.tmp.py  ## Create and open the basic generator expression example
	@$(EDITOR) "$<"

run_basic_genex: $$(subst run_,,$$@).tmp.py  #- Run the basic generator expression example
	@$(Spaces)
	"./$<"
	@$(Spaces)

basic_gen_equiv: $$@.tmp.py  ## Create and open the equivalent generator example
	@$(EDITOR) "$<"

run_basic_gen_equiv: $$(subst run_,,$$@).tmp.py  ## Run the the equivalent generator example
	@$(Spaces)
	"./$<"
	@$(Spaces)

_virtues_of_laziness_:  ## "Virtues of Laziness" segue
	@true

Shakespeare.txt:  # Download complete works of shakespeare
	curl -o Shakespeare.txt "https://www.gutenberg.org/files/100/100-0.txt"

ls_shakespeare: Shakespeare.txt  ## Show the size of the Shakespeare file
	@$(Spaces)
	ls -lh "Klein.txt" "Shakespeare.txt"
	@$(Spaces)

word_search_lc: $$@.tmp.py  ## Create and open the list comprehension version of word search
	@$(EDITOR) "$<"

word_search_gen: $$@.tmp.py  ## Create and open the generator version of word search
	@$(EDITOR) "$<"

run_word_search_lc: $$(subst run_,,$$@).tmp.py Shakespeare.txt  ## Run the list comprehension version of word search
	@$(Spaces)
	/usr/bin/time -l "./$<" "Shakespeare.txt" "beauty" 10 2>&1 | sed -ne '1,/maximum resident set size/ p'
	@$(Spaces)

run_word_search_gen: $$(subst run_,,$$@).tmp.py Shakespeare.txt  ## Run the generator expression version of word search
	@$(Spaces)
	@echo -n /usr/bin/time -l "./$<" "Shakespeare.txt" "beauty" 1000 2\>\&1 \| sed -ne \'1,/maximum resident set size/ p\' \| tail -13 | $(QuietCopy)
	/usr/bin/time -l "./$<" "Shakespeare.txt" "beauty" 10  2>&1 | sed -ne '1,/maximum resident set size/ p'
	@$(Spaces)
	@echo \(Copied\)

py_hi:  ## Measure Python printing 'hi'
	@$(Spaces)
	/usr/bin/time -l python -c "print('hi')" 2>&1 | head -3
	@$(Spaces)

echo_hi:  #- Measure echo printing 'hi'
	@$(Spaces)
	/usr/bin/time -l echo hi 2>&1 | head -3
	@$(Spaces)

show_good:  ## Show the "good code" section
	# @$(ReadAt) "### Good code"
	@open "https://github.com/inventhouse/tutorials/tree/master/PySG-Comprehensions#good-code"

# # #
clean:  #M Delete the .tmp.py files
	rm -f *.tmp.py

include sequence.tmp.mk
# # #
