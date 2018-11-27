# jq demos

# Doc comments start with double-hash
# 'make list' prints documented targets
# Meta-targets are documented with 'hash-M'
# 'make list_meta' prints these
# Many targets push the demo command to the pasteboard, cmd-v to paste/edit/run
# Sequential aliases are for easily running targets one-after-another with 'source ./makenext'
# 'make list_seq' prints these

default: list  #M Target to run if none is specified

SingleFile="Single.json"
FullFile="Full.json"

## Simple commands
cat_single:         ## Print the single-entry example
	cat $(SingleFile)

print_single:       ## Pretty-print the single-entry example
	cat $(SingleFile) | jq '.'

single_name:        ## Extract .name from single-entry example
	cat $(SingleFile) | jq '.name'
	@echo "NOTE: Don't forget the dot!"

single_length:      ## Get length of the single-entry example
	cat $(SingleFile) | jq 'length'

cat_full:           # Print the full example
	cat $(FullFile)

print_full:         # Pretty-print the full example
	cat $(FullFile) | jq '.'

full_length:        ## Get length of the full example
	cat $(FullFile) | jq 'length'

bad_full_names:     ## Full example is an array, this will error
	cat $(FullFile) | jq '.name'

##
## Arrays & slicing
NameFullCmd=cat $(FullFile) | jq '.[] | .name'
full_names:         ## Get name from each item in full example
	$(NameFullCmd)
	@echo "$(NameFullCmd)" | tr -d "\n" | pbcopy
	@echo "Copied: $(NameFullCmd)"
	@echo "NOTE: Also works as '.[].name'"

SliceCmd=cat $(FullFile) | jq '.[-3:]'
slice:              ## Get last 3 items
	$(SliceCmd)
	@echo "$(SliceCmd)" | tr -d "\n" | pbcopy
	@echo "Copied: $(SliceCmd)"
	@echo "NOTE: negative indexes and slicing work"

NameSliceCmd=cat $(FullFile) | jq '.[-3:] | .[].name'
name_slice:         ## Get name from last 3 items in full example
	$(NameSliceCmd)
	@echo "$(NameSliceCmd)" | tr -d "\n" | pbcopy
	@echo "Copied: $(NameSliceCmd)"
	@echo "NOTE: Requires '|'"

NameArrayCmd=cat $(FullFile) | jq '.[-3:] | [ .[] | .name ]'
name_array:         ## Get name from last 3 items in full example as an array
	$(NameArrayCmd)
	@echo "$(NameArrayCmd)" | tr -d "\n" | pbcopy
	@echo "Copied: $(NameArrayCmd)"
	@echo "NOTE: '| .[] | [ .name ]' makes multiple arrays"

##
## Dictionaries
NameDurationCmd=cat $(FullFile) | jq '[ .[] | { name, micros: .duration } ]'
name_duration:      ## Get name and micros from full example
	$(NameDurationCmd)
	@echo "$(NameDurationCmd)" | tr -d "\n" | pbcopy
	@echo "Copied: $(NameDurationCmd)"
	@echo "NOTE: 'name' (no dot!) is equivalent to 'name: .name'"

DelCmd=cat $(FullFile) | jq '[ .[] | del(.traceId, .id, .kind, .timestamp) ]'
del_fields:         ## Drop uninteresting fields from full example
	$(DelCmd)
	@echo "$(DelCmd)" | tr -d "\n" | pbcopy
	@echo "Copied: $(DelCmd)"
	@echo "NOTE: Re-boxed into an array"

##
## Filtering, sorting, grouping, max/min
MaxCmd=cat $(FullFile) | jq 'max_by(.duration)'
max_duration:       ## Finds the longest span
	$(MaxCmd)
	@echo "$(MaxCmd)" | tr -d "\n" | pbcopy
	@echo "Copied: $(MaxCmd)"
	@echo "NOTE: input to max_by is an array"

SelectCmd=cat $(FullFile) | jq '[ .[] | select(.duration > 300000000) ]'
select:             ## Extracts spans longer than 300s from the full example
	$(SelectCmd)
	@echo "$(SelectCmd)" | tr -d "\n" | pbcopy
	@echo "Copied: $(SelectCmd)"

RegexCmd=cat $(FullFile) | jq '[ .[] | select(.name | test(".*programs.*")) ]'
regex:              ## Extracts spans matching '.*programs.*' from the full example
	$(RegexCmd)
	@echo "cat $(FullFile) | jq '[ .[] | select(.name | test(\".*programs.*\")) ]'" | tr -d "\n" | pbcopy  # Using $(RegexCmd) loses vital quotes
	@echo "Copied: cat $(FullFile) | jq '[ .[] | select(.name | test(\".*programs.*\")) ]'"
	@echo "NOTE: select takes a filter expression; match() produces match objects, see manual for more"

SortCmd=cat $(FullFile) | jq 'sort_by(.duration) | .[-5:]'
sort:               ## Extract 5 longest spans
	$(SortCmd)
	@echo "$(SortCmd)" | tr -d "\n" | pbcopy
	@echo "Copied: $(SortCmd)"
	@echo "NOTE: input to sort_by is an array, .duration is a path into an item in that array"

GroupCmd=cat $(FullFile) | jq 'group_by(.name)'
group_name:         ## Group spans by name
	$(GroupCmd)
	@echo "$(GroupCmd)" | tr -d "\n" | pbcopy
	@echo "Copied: $(GroupCmd)"
	@echo "NOTE: input to group_by is an array, .name is a path into an item in that array, produces array-of-arrays"

##
## Variables, functions
rel_time:           ## Convert timestamps to relative
	cat $(FullFile) | jq 'min_by(.timestamp).timestamp as $$first_ts | [ .[] | { name, duration, rel_time: ((.timestamp - $$first_ts) / 1000000) } ]'
	@echo "cat $(FullFile) | jq 'min_by(.timestamp).timestamp as \$$first_ts | [ .[] | { name, duration, rel_time: ((.timestamp - \$$first_ts) / 1000000) } ]'" | tr -d "\n" | pbcopy  # '$' is a pain in make
	@echo "Copied: cat $(FullFile) | jq 'min_by(.timestamp).timestamp as \$$first_ts | [ .[] | { name, duration, rel_time: ((.timestamp - \$$first_ts) / 1000000) } ]'"
	@echo "NOTE: min_by returns the whole object, .timestamp to extract the micros; unbox the original array, build objects and re-box"

def_utos:           ## Convert duration to seconds using a function
	cat $(FullFile) | jq 'def uToS($$u): $$u / 1000000; sort_by(.duration) | .[].duration |= uToS(.)'
	@echo "cat $(FullFile) | jq 'def uToS(\$$u): \$$u / 1000000; sort_by(.duration) | .[].duration |= uToS(.)'" | tr -d "\n" | pbcopy
	@echo "Copied: cat $(FullFile) | jq 'def uToS(\$$u): \$$u / 1000000; sort_by(.duration) | .[].duration |= uToS(.)'"
	@echo "NOTE: No '|' after 'def' statement, '|=' is update-assignment"

##
## Put it all together
the_works:          ## Longest span of each name
	cat $(FullFile) | jq -f "LongestByName.jq"

the_works_explain:  ## Display the LongestByName program
	cat "LongestByName.jq"
	@echo "NOTE: You can put long programs into a file and have comments!"

##
## Gotchas
cat_names:          ## Print the names.txt file
	cat names.txt
	@echo "NOTE: Simple list of names to make into json objects"

BadNameObjectsCmd=cat names.txt | jq '[ { name: . } ]'
bad_name_objects:   ## Make array of objects from a list of names, badly
	$(BadNameObjectsCmd)
	@echo "$(BadNameObjectsCmd)" | tr -d "\n" | pbcopy
	@echo "Copied: $(BadNameObjectsCmd)"
	@echo "NOTE: Runs filter for each line in names.txt"

NameObjectsCmd=cat names.txt | jq -s '[ .[] | { name: . } ]'
name_objects:       ## Actually make array of objects from a list of names
	$(NameObjectsCmd)
	@echo "$(NameObjectsCmd)" | tr -d "\n" | pbcopy
	@echo "Copied: $(NameObjectsCmd)"
	@echo "NOTE: -s 'slurps' items into an array, which can then be iterated and re-boxed"

unwrap_object:      ## Unwrapping an object gives you a pile of various values
	cat $(SingleFile) | jq '.[]'
	@echo "NOTE: Unwrapping an object works, but probably won't be what you want"

##
## Common errors
errors:             ## Show some common errors
	-echo '{ "name": "foo" }' | jq 'name'
	@echo "NOTE: Forgot the dot, should be .name"
	@echo
	-echo '[{ "name": "foo" }]' | jq '.name'
	@echo "NOTE: Need to iterate array"
	@echo
	-echo '{ "name": "foo" }' | jq '.name ]'
	@echo "NOTE: Rarely actually a shell quoting issue"
	@echo

recap:              ## Prompt to finish with recap
	@echo "Recap"


# # #  Meta-targets  # # #
list:          #M Lists the documented targets
	@egrep "^(\w+:(\s+\w+)*\s+)?##" Makefile

list_meta:     #M Lists the meta-targets
	@egrep "^\w+:(\s+\w+)*\s+#M" Makefile

list_all:      #M Lists all targets
	@egrep "^\w+:" Makefile

list_seq:      #M Lists the numbered aliases
	@egrep "^\d+:" Makefile

aliases:       #M Re-create the sequence aliases from documented targets, must be copy-pasted into Makefile
	@egrep "^\w+:\s+##" Makefile | cut -d ":" -f 1 | cat -n | sed -n -E 's/^[[:space:]]+([[:digit:]]+)[[:space:]]+(.+)/\1: \2/gp'

better_aliases: # Re-create the sequence aliases from documented targets, must be copy-pasted into Makefile - recognize targets with dependencies and preserve doc comments; still wouldn't find targets with multiple things before the ':'
	@egrep "^\w+:(\s+\w+)*\s+##" Makefile | cat -n | sed -n -E 's/^[[:space:]]+([[:digit:]]+)[[:space:]]+([^:]+):([^#]+)#(#.*)/\1: \2  \4/gp'  # HACK: make sure aliases don't use hash-hash comments (maybe doesn't matter if I move to imported aliases?)


# # #  Sequential aliases  # # #
1: cat_single
2: print_single
3: single_name
4: single_length
5: full_length
6: bad_full_names
7: full_names
8: slice
9: name_slice
10: name_array
11: name_duration
12: del_fields
13: max_duration
14: select
15: regex
16: sort
17: group_name
18: rel_time
19: def_utos
20: the_works
21: the_works_explain
22: cat_names
23: bad_name_objects
24: name_objects
25: unwrap_object
26: errors
27: recap

# # #
