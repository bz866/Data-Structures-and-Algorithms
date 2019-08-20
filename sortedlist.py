<<<<<<< HEAD
# Implementation of the self-sorted list
class sortedList:
	# Creates an empty list instance
	def __init__(self):
		self._theElements = list()



	# Modified version of the binary search that returns the index within 
	# a sorted sequence indicating where the target should be located
	def _findSortedPositon(self, target):
		left = 0
		right = len(self._theElements) - 1
		while left <= right:
			mid = (left + right) // 2 
=======
# Implementation of the sorted list ADT
class sortedList:
	# Create a empty list instance
	def __init__(self):
		self._theElements = list()
	
	# Returns the number of items in the sorted list
	def __len__(self):
		return len(self._theElements)
	
	# Determines if an element is in the sorted list using binary search
	def __contains__(self, target):
		ndx = self._binarySearchPosition(target)
		return ndx < len(self._theElements) and self._theElements[ndx] == target
	
	# Adds a new unique element to the set
	def add(self, newValue):
		ndx = self._binarySearchPosition(newValue)
		self._theElements.insert(ndx, newValue)
		
	# Removes an element from the list
	def remove(self, valueToRemove)
		ndx = self._binarySearchPosition(valueToRemove)
		# the value to remove must be in the list
		assert ndx < len(self._theElements) and self._theElements[ndx] == valueToRemove
		self._theElements.pop(ndx)
		
	# Determines if this set is a subset of setB
	def isSublist(self, listB):
		if len(listB) > len(self._theElements): # if the setB is longer, no way to be a sublist
			return False
		for i in listB:
			if not self.__contains__(i):
				return False 
		return True
	
	# Determines if two list are equal
	def __eq__(self, listB)
		if len(self._theElements) != len(listB):
			return False
		else:
			return self.isSublist(listB)
		
	# Returns an Iterator for traversing the sorted list of items
	def __iter__(self):
		return _SortedListIterator(self._theElements)
	
	# Modified version of the binary search that returns the index within 
	# a sorted sequence indicating where the target should be located 
	def _binarySearchPosition(target):
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

		return left # index where the target should be to form a sorted list

# An Iterator for sorted list ADT
class _SortedListIterator:
	def __init__(self, theSortedList):
		self._sortedListRef = theSortedList
		self._curNdx = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self._curNdx < len(self._sortedListRef):
			entry = self._sortedListRef[self._curNdx]
			self._curNdx += 1
			return entry
		else:
			raise StopIteration
