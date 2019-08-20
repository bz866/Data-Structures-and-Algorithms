# Insertion Sort
# - Iterate the sequence several times
# - Keep picking up the head of the subsequence
# - Place the picked element to its proper sorted position
# The insertion sort maintains a collection of sorted items and a collection of items to be sorted
# The algorithm maintains both the sorted and unsorted collections within the same sequence structure
# The algorithms keeps the list of sorted values at the front of the sequences and picks the next unsorted value from the first of those yet to be positioned
# To position the next item, the corrent spot within the sequence of sorted values is found by performing a search
# After finding the proper position, the slot has to be opened by shifting the items down one position

import warnings

# Implementation of insertion sort algorithm
def insertionSort(theValues):
	if len(theValues) == 0:
		warnings.warn("User is sorting empty sequence.")
		
	n = len(theValues)
	# Start with the first element as sorted 
	for i in range(1, n):
		valueToInsert  = theValues[i]
		posToInsert = i
		# Find the right positon to insert the value
		while posToInsert > 0 and valueToInsert < theValues[posToInsert - 1]: 
			theValues[posToInsert] = theValues[posToInsert - 1]
			posToInsert -= 1
		theValues[posToInsert] = valueToInsert

	return theValues