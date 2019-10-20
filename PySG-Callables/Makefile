# Example Makefile

default: list  #M Target to run if none is specified

# Requires https://github.com/inventhouse/MakeDemo
# $ path/to/MakeDemo/demoinit
# $ source ./demonow
include $(MakeDemoDir)/MakeDemo.make
ChunkFile := "README.md"
CodeFile := "code_chunks.py"
CodeChunk = $(GetChunk) $(CodeFile)
# EDITOR := cat
EDITOR := code
Spaces = echo; echo

%.tmp.py:
	@$(CodeChunk) header > "$@"
	@$(CodeChunk) "$(@:.tmp.py=)" >> "$@"
	@chmod a+x "$@"

.SECONDEXPANSION:

Intro:  ## What is this talk about?
	$(AtChunk)

Callables:  ## What the heck are callables?
	$(AtChunk)

Snippets:  ## "Snippets of code"
	$(AtChunk)

caesar_function: $$@.tmp.py  ## Basic function demo
	@$(EDITOR) "$<"

run_caesar_function: $$(subst run_,,$$@).tmp.py  ## Run the basic function demo
	@$(Spaces)
	"./$<"
	@$(Spaces)

Code_with_data:  ## Ways of grouping code together with data
	@$(ChunkNamed) "$(subst _, ,$@)"

caesar_class: $$@.tmp.py  ## Class demo
	@$(EDITOR) "$<"

run_caesar_class: $$(subst run_,,$$@).tmp.py  ## Run class demo
	@$(Spaces)
	"./$<"
	@$(Spaces)

fibonacci_gen: $$@.tmp.py  ## Generator demo
	@$(EDITOR) "$<"

run_fibonacci_gen: $$(subst run_,,$$@).tmp.py  ## Run generator demo
	@$(Spaces)
	"./$<"
	@$(Spaces)

caesar_closure: $$@.tmp.py  ## Closure demo
	@$(EDITOR) "$<"

run_caesar_closure: $$(subst run_,,$$@).tmp.py  ## Run closure demo
	@$(Spaces)
	"./$<"
	@$(Spaces)

Code_as_data:  ## Ways of using code AS data
	@$(ChunkNamed) "$(subst _, ,$@)"

caesar_bound: $$@.tmp.py  ## Bound method demo
	@$(EDITOR) "$<"

run_caesar_bound: $$(subst run_,,$$@).tmp.py  ## Run bound method demo
	@$(Spaces)
	"./$<"
	@$(Spaces)

Vigenère: $$@.tmp.py  ## Vigenère demo
	@$(EDITOR) "$<"

run_Vigenère: $$(subst run_,,$$@).tmp.py  ## Run Vigenère demo
	@$(Spaces)
	"./$<"
	@$(Spaces)

# # #
clean:  #M Delete the .tmp.py files
	rm -f *.tmp.py

include sequence.tmp.mk
# # #
