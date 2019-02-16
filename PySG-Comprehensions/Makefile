# PySG Comprehensions Makefile
# Copyright (c) 2019 Benjamin Holt -- MIT License

default: list  #M Target to run if none is specified

# Requires https://github.com/inventhouse/MakeDemo
# $ source ./demonow

include $(MakeDemoDir)/MakeDemo.make
ChunkFile := "code_chunks.py"
EDITOR := cat
EditorAt := "$(MakeDemoDir)/atom_at"
ReadFile := "README.md"
ReadAt = $(EditorAt) $(ReadFile)
# ReadChunk = $(GetChunk) "README.md"

%.tmp.py:
	@$(ChunkNamed) header > "$@"
	@$(ChunkNamed) "$(@:.tmp.py=)" >> "$@"
	@chmod a+x "$@"

.SECONDEXPANSION:

## Basics ##
intro:  # # Open the README with the lesson outline
	@$(EDITOR) README.md

show_klein:  ## Show the lines we'll be working with
	cat Klein.txt

show_what:  ## Show the "what are they?" section
	@$(ReadAt) "### What are they?"

basic_lc: $$@.tmp.py  ## Create and open basic listcomp example
	@$(EDITOR) "$<"

run_basic_lc: $$(subst run_,,$$@).tmp.py  ## Run the basic listcomp example
	"./$<"

basic_for: $$@.tmp.py  ## Create and open equivalent basic for-loop example
	@$(EDITOR) "$<"

run_basic_for: $$(subst run_,,$$@).tmp.py  ## Run the equivalent basic for-loop example
	"./$<"

basic_map_filter: $$@.tmp.py  ## Create and open equivalent basic map-filter example
	@$(EDITOR) "$<"

run_basic_map_filter: $$(subst run_,,$$@).tmp.py  ## Run the equivalent basic map-filter example
	"./$<"

## Trickier ##
show_tricky:  ## Show the "getting tricky" section
	@$(ReadAt) "### Getting tricky"

tuple_lc: $$@.tmp.py  ## Create and open comp over tuples example
	@$(EDITOR) "$<"

run_tuple_lc: $$(subst run_,,$$@).tmp.py  ## Run the comp over tuples example
	"./$<"

tuple_for: $$@.tmp.py  # # Create and open equivalent loop over tuples example
	@$(EDITOR) "$<"

run_tuple_for: $$(subst run_,,$$@).tmp.py  # # Run the equivalent basic loop over tuples example
	"./$<"

new_tuple_lc: $$@.tmp.py  ## Create and open new tuples example
	@$(EDITOR) "$<"

run_new_tuple_lc: $$(subst run_,,$$@).tmp.py  ## Run the new tuples example
	"./$<"

two_kinds_of_if: $$@.tmp.py  ## Create and open two kinds of if example
	@$(EDITOR) "$<"

run_two_kinds_of_if: $$(subst run_,,$$@).tmp.py  ## Run the two kinds of if example
	"./$<"

slice_assign_viz:  ## Copy slice-assignment example and open pythontutor.com
	@echo "Copying $@, paste into pythontutor"
	$(AtChunk) | $(QuietCopy)
	open "http://pythontutor.com/visualize.html#mode=edit"

slice_assign_walk: $$@.tmp.py  ## Create and open slice assign example
	@$(EDITOR) "$<"

run_slice_assign_walk: $$(subst run_,,$$@).tmp.py  ## Run the slice assign example
	"./$<" ..

## Nesting ##
show_nesting:  ## Show the "nesting" section
	@$(ReadAt) "### Nesting"

matrix_lc: $$@.tmp.py  ## Create and open matrix example
	@$(EDITOR) "$<"

run_matrix_lc: $$(subst run_,,$$@).tmp.py  ## Run the matrix example
	"./$<"

combinations_for: $$@.tmp.py  ## Create and open equivalent combinations loop example
	@$(EDITOR) "$<"

run_combinations_for: $$(subst run_,,$$@).tmp.py  ## Run the equivalent combinations loop example
	"./$<"

combinations_lc: $$@.tmp.py  ## Create and open combinations listcomp example
	@$(EDITOR) "$<"

run_combinations_lc: $$(subst run_,,$$@).tmp.py  ## Run the combinations listcomp example
	"./$<"

## Other Types ##
show_other:  ## Show the "other types" section
	@$(ReadAt) "### Other types"

set_comp: $$@.tmp.py  ## Create and open set comprehension example
	@$(EDITOR) "$<"

run_set_comp: $$(subst run_,,$$@).tmp.py  ## Run the set comprehension example
	"./$<"

dict_comp: $$@.tmp.py  ## Create and open dict comprehension example
	@$(EDITOR) "$<"

run_dict_comp: $$(subst run_,,$$@).tmp.py  ## Run the dict comprehension example
	"./$<"

## Generator Expressions ##
show_gen:  ## Show the "generator expressions" section
	@$(ReadAt) "### Generator expressions"

genex_viz:  ## Copy generator expression example and open pythontutor.com
	@echo "Copying $@, paste into pythontutor"
	$(AtChunk) | $(QuietCopy)
	open "http://pythontutor.com/visualize.html#mode=edit"

basic_genex: $$@.tmp.py  ## Create and open the basic generator expression example
	@$(EDITOR) "$<"

run_basic_genex: $$(subst run_,,$$@).tmp.py  ## Run the basic generator expression example
	"./$<"

basic_gen_equiv: $$@.tmp.py  ## Create and open the equivalent generator example
	@$(EDITOR) "$<"

run_basic_gen_equiv: $$(subst run_,,$$@).tmp.py  ## Run the the equivalent generator example
	"./$<"

Shakespeare.txt:  # Download complete works of shakespeare
	curl -o Shakespeare.txt "https://www.gutenberg.org/files/100/100-0.txt"

word_search_lc: $$@.tmp.py  ## Create and open the list comprehension version of word search
	@$(EDITOR) "$<"

run_word_search_lc: $$(subst run_,,$$@).tmp.py Shakespeare.txt  ## Run the list comprehension version of word search
	/usr/bin/time -l "./$<" "Shakespeare.txt" "beauty" 10 2>&1 | head -13

word_search_gen: $$@.tmp.py  ## Create and open the generator expression version of word search
	@$(EDITOR) "$<"

run_word_search_gen: $$(subst run_,,$$@).tmp.py Shakespeare.txt  ## Run the generator expression version of word search
	/usr/bin/time -l "./$<" "Shakespeare.txt" "beauty" 10  2>&1 | head -13

py_hi:  ## Measure Python printing 'hi'
	/usr/bin/time -l python -c "print('hi')" 2>&1 | head -3

show_good:  ## Show the "good code" section
	@$(ReadAt) "### Good code"

echo_hi:  # Measure echo printing 'hi'
	/usr/bin/time -l echo hi 2>&1 | head -3

# # #
clean:  #M Delete the .tmp.py files
	rm -f *.tmp.py

include sequence.tmp.mk
# # #
