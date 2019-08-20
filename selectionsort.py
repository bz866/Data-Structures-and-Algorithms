# Selection Sort 
# An improvement on the bubble sort
# - Assume the sequence contains n values 
# - iterate the sequence multiple times
# - Only do ONE swap per walking through (improvement on the bubble sort)
# - always get the smallest value and put it in the head of the sebsequence
# Time: O(n^2)
# Space: O(1) 

import warnings

# Implementation of the selection sort algorithm
def selectionSort(theValues):
	if len(theValues) == 0:
		warnings.warn("User is sorting empty sequence.")
		
	n = len(theValues)
	for i in range(0, n):
		theSmallestNdx = i
		for j in range(i, n):
			if theValues[j] < theValues[theSmallestNdx]:
				theSmallestNdx = j
		# Swap the smallest value to the head of the subsequence
		temp = theValues[i]
		theValues[i] = theValues[theSmallestNdx]
		theValues[theSmallestNdx] = temp
	
	return theValues