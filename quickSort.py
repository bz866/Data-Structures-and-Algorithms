# Implementation of the quick sort algorithm
def quickSort(theList):
	n = len(theList)
	recQuickSort(theList, 0, n-1)


# The recursion implementation using virtual segments
def recQuickSort(theList, first, last):
	# Check the base case
	if first >= last:
		return 

	else:
		# Save the pivot value 
		pivot = theList[first]

		# partition the sequence and obtain the pivot position
		pos = partitionList(theList, first, last)

		# Repeat the process on the two subsequence
		recQuickSort(theList, first, pos - 1)
		recQuickSort(theList, pos + 1, last)

# partitions the subsequence using the first key as the pivot
def partitionList(theList, first, last):
	# Save a copy of the pivot table
	pivot = theList[first]

	# Find the pivot position and move the elements around the pivot
	left = first + 1
	right = last
	while left <= right:
		# Find the first key larger than the pivot
		while left < right and theList[left] < pivot:
			left += 1

		# Find the last key in the sequence that is smaller than the pivot
		while right >= left and theList[right] >= pivot:
			right -= 1

		# Swap the two keys if we have not completed this partition
		if left < right:
			tmp = theList[left]
			theList[left] = theList[right]
			theList[right] = tmp

	# Put the pivot in the proper position
	if right != first:
		theList[first] = theList[right]
		theList[right] = pivot

	# Returns the index position of the pivot value 
	return right

	