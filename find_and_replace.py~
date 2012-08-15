#Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. Itcan 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by create_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
	return [match, replacement]


def apply_converter(converter, string):
  	if string.find(converter[0]) == -1:
		return string
	else:
		string = string.replace(converter[0], converter[1])
		return apply_converter(converter, string)

										# For example,

c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
										#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
										#>>> ab
c2 = make_converter('duplicate', 'DD')
print apply_converter(c2, 'all duplicates will be replaced with non-duplicates as soon they can be duplicated')
										# Note that this process is not guaranteed to terminate for all inputs
										# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
										# run forever).
