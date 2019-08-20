# Bubble Sort
# - Assume the sequence contains n values
# - iterate the sequence multiple times 
# - swap values if back > front (bubble) 
# - Time: O(n^2)
# - [(n -1) + 1] * [(n - 1 + 1) / 1 + 1] / 2
# - 0.5 * n^2 + 0.5 * n
# - Spac: O(1)
# - sorting done by swapping

import warnings

# implementation of the bubble sort algorithm
def bubbleSort(theValues):
	if len(theValues) == 0:
		warnings.warn("User is sorting empty sequence.")

	n = len(theValues)
	for i in range(0, n - 1):
		for j in range(0, n - i - 1):
			if theValues[j] > theValues[j+1]:
				# Swap
				temp = theValues[j]
				theValues[j] = theValues[j+1]
				theValues[j+1] = temp
	return theValues


