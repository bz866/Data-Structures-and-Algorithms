# Implementation of the Set ADT container using a Python list

class Set:
	# Creates an empty set instance
	def __init__(self):
		self._theElements = list()

	# Returns the number of items in the set
	def __len__(self):
		return len(self._theElements)

	# Determines if an element is in the set
	def __contains__(self, element):
		return element in self._theElements

	# Adds a new unique element to the set
	def add(self, element):
		self._theElements.append(element)

	# Removes an element from the set
	def remove(self, element):
		assert element in self, "The element must be in the set."
		self._theElements.remove(item)

	# Determines if this set is a subset of the other set
	def isSubsetOf(self, setB):
		for element in self._theElements:
			if element not in setB:
				return False
		return True

	# Determines if two sets are equal 
	def __eq__(self, setB):
		if len(self) != len(setB):
			return False 
		else:
			return self.isSubsetOf(setB)

	# Creates a new set from the union of this set and setB; s | b
	def union(self, setB):
		newSet = Set()
		newSet._theElements.extend(self._theElements)
		for e in setB:
			if e not in self._theElements:
				newSet.add(e)
		return newSet

	# Creates a new set from the intersection: self set and setB; s & b
	def interset(self, setB):
		# Time: O(mn); Space(max(m, n))
		newSet = Set()
		newSet._theElements.extend(setB._theElements)
		for e in setB:
			if e not in self._theElements:
				newSet.remove(e)
		return newSet

	# Creates a new set from the difference: self set and setB; self set - setB
	def difference(self, setB):
		# Time: O(mn); Space(max(m, n))
		newSet = Set()
		newSet._theElements.extend(self._theElements)
		for e in self._theElements:
			if e in setB._theElements:
				newSet.remove(e)
		return newSet

	#Returns an iterator for traversing the list of items
	def __iter__(self):
		return _SetIterator(self._theElements)

# An Iterator for Set ADT
class _SetIterator:
	def __init__(self, theSet):
		self._setRef = theSet
		self._curNdx = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self._curNdx < len(self._setRef):
			entry = self._setRef[self._curNdx]
			self._curNdx += 1
			return entry
		else:
			raise StopIteration





