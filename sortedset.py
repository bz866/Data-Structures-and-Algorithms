# Implementation of the sorted Set ADT using a sorted list
class sortedSet:
	# Creates an empty set instance
	def __init__(self):
		self._theElements = list()

 	# Returns the number of items in the set
	def __len__(self):
		return len(self._theElements)
	
	# Determines if an element is in the set
	def __contains__(self, target):
		ndx = self._binarySearchPosition(target)
		return ndx < len(self._theElements) and self._theElemets[ndx] == target
	
	# Adds a new unique element to the set
	def add(self, newValue):
		ndx = self._findPosition(newValue)
		if not (ndx < len(self._theElements) and self._theElemets[ndx] == newValue): # new value not in the set
			self._theElements.insert(ndx, newValue)
	
	# Removes a element from the set
	def remove(self, newValue):
		ndx = self._findPosition(newValue)
		assert ndx < len(self._theElements) and self._theElemets[ndx] == newValue, "The element to be removed must in the set"
		self._theElements.pop(ndx)
		
	# Determines if this set is a subset of setB
	def isSubset(self, setB):
		if len(self._theElements) > len(setB._theElements): # if longer, no way to be a subset
			return False
		
		for element in self._theElements:
			if element not in setB:
				return False
		return True
	# Determines if two sets are equal
	def __eq__(self, setB):
		if len(self._theElements) != len(setB._theElements):
			return False
		else:
			for i in range(len(self._theElements)):
				if self._theElements[i] != setB._theElements[i]:
					return False
			return True
		
	# Get a new set as the union of two sets
	def union(self, setB):
		newSet = sortedSet()
		ptrA = 0
		ptrB = 0
		while ptrA < len(self._theElements) and ptrB < len(setB._theElemnets):
			valueA = self._theElements[ptrA]
			valueB = setB._theElements[ptrB]
			if valueA < valueB:
				newSet._theElements.append(valueA)
				ptrA += 1
			elif value > valueB:
				newSet._theElements.append(valueB)
				ptrB += 1
			else: # only one of the two duplicates are appended
				newSet._theElements.append(valueA)
				ptrA += 1
				ptrB += 1
		
		# If setA contains more items, append them to newSet
		while a < len(self._theElements):
			newSet._theElements.append(self._theElements[ptrA])
			a += 1
		
		# Or if setB contains more items, append them to newSet
		while b < len(self._theElements):
			newSet._theElements.append(self._theElements[ptrB])
			b += 1
			
		return newSet
	
	# Modified version of the bianry search that returns the index within 
	# a sorted sequence indicating where the target should be located
	def _binarySearchPosition(self, target):
		left = 0
		right = len(self._theElements) - 1
		while left <= right:
			mid = (left + right) // 2
			if self._theElements[mid] < target:
				left = left + 1
			elif self._theElements[mid] > target:
				right = right - 1
			else: # found
				return mid
		
		return left # the index where the target value should be
	
