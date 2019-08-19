# Implementation of the linear search on an unsorted sequence 
def linearSearch(theValues, target):
	# Time: O(n)
	# Space: O(1)
	for i in theValues:
		if theValues[i] == target: # if the target is in the ith element, return True
			return True

	return False # not found

# implementation of the linear search on a sorted sequence in ascending order 
def ascendingSortedLinearSearch(theValues, target):
	# Time: O(n)
	# Space: O(1)
	if len(theValues) == 0: # empty sequence
		return False 

	elif len(theValues) == 1: # sequence that only has one element 
		if theValues[0] == target:
			return True
		else:
			return False

	elif len(theValues0) > 1: # sequence that has more than one element 
		for i in range(0, len(theValues)):
			if theValues[i] == target:
				return True
			elif theValues[i] > target:
				return False # not found

	return False # not found and all elements smaller than the target

# implementation of the linear search on a sorted sequence in descending order
def descendingSortedLinearSearch(theValues, target): 
	# Time: O(n)
	# Space: O(1)
	if len(theValues) == 0: # empty sequence
		return False 

	elif len(theValues) == 1: # sequence that only has one element 
		if theValues[0] == target:
			return True
		else:
			return False

	elif len(theValues0) > 1: # sequence that has more than one element 
		for i in range(0, len(theValues)):
			if theValues[i] == target:
				return True
			elif theValues[i] < target:
				return False # not found 

	return False # not found and all elements smaller than the target

# Searching for the smallest value in an unsorted sequence
def findSmallest(theValues):
	# Time: O(n)
	# SpaceL O(1)
	assert len(theValues) > 0, "The given sequence must have length > 0"
	smallest = theValues[0]
	for i in range(0, len(theValues)): # traverse the sequence
		if smallest > theValues[i]: # update the smallest
			smallest = theValues[i]

	return smallest

# Implementation of the binary search algorithm
def binarySearch(theValues, target):
	# Time: O(logn)
	# Space: O(1)
	if len(theValues) == 0: # empty sequence
		return False 
	
	# start with the entire sequence of elements
	head = 0
	tail = len(theValues) - 1
	while head <= tail: # search until the sequence cannot be subdivided further
		mid = (head + tail) // 2
		if theValues[mid] == target:
			return True
		elif theValues[mid] < target:
			head = mid + 1
		elif theValues[mid] > target:
			tail = mid - 1

	return False # not found 




