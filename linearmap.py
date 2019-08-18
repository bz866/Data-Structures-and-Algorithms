# Implementation of Map ADT using a single list 

class Map:
	# Creates an empty map instance
	def __init__(self):
		self._entryList = list()

	# Returns the number of entries in the map
	def __len__(self):
		return len(self._entryList)

	# Determines if the map contains the given key
	def __contains__(self, key):
		return self._findPosition(key) is not None

	# Adds a new entry to the map if the key does exist. Otherwise, the new value replaces the 
	# current value associated with the key
	def add(self, key, value):
		ndx = self._findPosition(key)
		if ndx is None: # new entry
			newEntry = _MapEntry(key, value)
			self._entryList.append(newEntry)
		else; # exited entry
			self._entryList[ndx].value = value

	# Returns the value associated with the key
	def valueOf(self, key):
		ndx = self._findPosition(key)
		assert ndx is not None, "Invalid map key."
		return self._entryList[ndx].value

	# Removes the entry asscociated with the key
	def remove(self, key):
		ndx = self._findPosition(key)
		assert ndx is not None, "Invalid map key."
		self._entryList.pop(ndx)

	# Returns an iterator for traversing the keys in the map
	def __iter__(self):
		return _MapIterator(self._entryList)

	# Helper method used to find the index position of a category. If the key is not found
	# None is returned 
	def _findPosition(self, key):
		for i in range(0, len(self._entryList)):
			# determines if the key is in the ith entry
			if self._entryList[i].key == key:
				return i
		# When not found, return None 
		return None 

# Storage class for holding the key/value pairs
class _MapEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value

# An Iterator for Map ADT
class _MapIterator:
	def __init__(self, theMap):
		self._mapRef = theMap
		self._curNdx = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self._curNdx < len(self._mapRef):
			entry = self._mapRef[self._curNdx]
			self._curNdx += 1
			return entry
		else:
			raise StopIteration


			


