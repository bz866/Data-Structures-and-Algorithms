# Implementation of merging two sorted lists
# Time: O(m+n)
# Space: (m+n)
def mergeSortedLists(listA, listB):
	newList = list()
	ptrA = 0 
	ptrB = 0

	# Merge the tow lists together until one is empty
	while ptrA < len(listA) and ptrB < len(listB):
		if listA[ptrA] < listB[ptrB]:
			newList.append(listA[ptrA])
			ptrA += 1
		else:
			newList.append(listB[ptrB])
			ptrB += 1

	# If list A contains more items, append to newList
	while ptrA < len(listA):
		newList.append(listA[ptrA])
		ptrA += 1

	# If list B contains more items, append to newList
	while ptrB < len(listB):
		newList.append(listB[ptrB])
		ptrB += 1

	return newList