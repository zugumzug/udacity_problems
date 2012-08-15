#Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(k):
	if k == []:
		return None
	current = [k[0], 0]
	following = [None, 0]
	for x in k:
		if x == current[0] and following[1] <= current[1]:
			current[1] += 1
		elif x != current[0]:
			if x == following[0]:
				following[1] += 1
				if following[1] > current[1]:
					current, following = following, [None, 0]
				elif x != following[0]:
					following = [x, 1]
	return current[0]




																																											#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
																																											# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
																																											# b

print longest_repetition([1,2,3,4,5])
																																											# 1

print longest_repetition([])

print longest_repetition([3,3,3,2,2,2,3,3,3,3])

