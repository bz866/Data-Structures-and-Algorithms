# Implementation of merge sort ‘
# Sorts a virtual subsequence in ascending order using merge sort
def recMergeSort(theSeq, first, last tmpArray):
	# The elements that comprise the virtual subsequence are indicated by the [first ... last]. tmpArray is temporary storage used in the 
	# merging phase of the merge sort algorithm 

	# Check the base case: the virtual sequence contains a single item
	if first == last:
		return;

	# sortable
	mid = (first + last) // 2

	# Split the sequence and perform the recursive step 
	recMergeSort(theSeq, first, mid, tmpArray)
	recMergeSort(theSeq, mid, last, tmpArray)

	# Merge the two ordered subsequence
	mergeVirtualSeq(theSeq, first, mid+1, last+1, tmpArray)

# Merges the two sorted virtual subsequence: [left .. right) [right..end)
# using the tmpArray for intermediate storage
def mergeVirtualSeq(theList, left, right, end, tmpArray):
	# Initialize two subsequence index variables
	a = left
	b = right 
	# Initialize an index variable for the resulting merged array
	m = 0
	# Merge the two sequences together until one is empty
	while a < right and b < end:
		if theSeq[a] < theSeq[b]:
			tmpArray[m] = theSeq[a]
			a += 1
		else:
			tmpArray[m] = theSeq[b]
			b += 1
		m += 1	

	# if the left subsequence contians more items append them to tmpArray
	while a < right:
		tmpArray[m] = theSeq[a]
		a += 1
		b += 1

	# if the right subsequence contains more
	while b < end:
		tmpArray[m] = theSeq[b]
		b += 1
		m += 1

	# Copy the sorted subsequence back into the original sequence structure
	for i in range(end - left):
		theSeq[i + left] = tmpArray[i]


# implementation of merge sort algorithm or use with Python lists
def outdatedMergeSort(theList):
	# Check the base case - the list contains only one item
	if len(theList) <= 1:
		return theList

	# the list contains more than one list so that it can be sorted
	# Compute the mid point
	mid = len(theList) // 2

	# Split the list and perform recursive step
	# Note: this implementation need logn times of copy subsequence so it's space complexity expensive
	leftHalf = outdatedMergeSort(theList[:mid])
	rightHalf = outdatedMergeSort(theList[mid:])

	# merge the two ordered sublists
	newList = mergeOrderedList(leftHalf, rightHalf)
	return newList

# Implementation of merge the two sorted subsequence
def mergeOrderedList(listOne, listTwo):
	if not listOne and not listTwo:
		return listOne
	elif listOne and not listTwo:
		return listOne
	elif not listOne and listTwo:
		return listTwo

	# both listOne and listTwo are not empty
	ptrOne = 0
	ptrTwo = 0
	mergedList = []
	# merge two lists elements one by one 
	while ptrOne < len(listOne) and ptrTwo < len(listTwo): 
		elementOne = listOne[ptrOne]
		elementTwo = listTwo[ptrTwo]
		if elementOne <= elementTwo:
			mergedList.append(elementOne)
			ptrOne += 1
		elif elementOne > elementTwo:
			mergedList.append(elementTwo)
			ptrTwo += 1

	# if listOne contains more elements
	while ptrOne < len(listOne):
		mergedList.extend(listOne[ptrOne:])

	# if listTwo contains more elements
	while ptrTwo < len(listTwo):
		mergedList.extend(listTwo[ptrTwo:])

	return mergedList