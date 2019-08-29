# Implementation of the Map ADT using closed hashing and a probe with double hashing
from arrays import Array

class HashMap:
	# Defines contants to represent the status of each table entry
	UNUSED = None 
	EMPTY = _MapEntry(None, None)
	
	# Creates an empty map instance
	def __init__(self):
		self._table = Array(7)
		self._count = 0
		self._maxCount = len(self._table) - len(self._table) // 3
		
	# Returns the number of entries in the map
	def __len__(self):
		return self._count
	
	# Determines if themap contains the given key
	def __contains__(self, key):
		slot = self._findSlot(key, False)
		return slot is not None
	
	# Adds a new entry to the map if the key does not exist. Otherwise, the new value replaces the current 
	# value associated with the key
	def add(self, key, value):
		if key in self:
			slot = self._findSlot(key, False)
			self._table[slot].value = value 
			return False
		else:
			slot = self._findSlot(key, True)
			self._table[slot] = _MapEntry(key, value)
			self._count += 1
			if self._count == self._maxCount:
				self._rehash()
			return True
		
	# Returns the value associated with the key
	def valueOf(self, key):
		slot = self._findSlot(key, False)
		assert slot is not None, "Invalid map key."
		return self._table[slot].value
	
	# Removes the entry associated with the key
	def remove(self, key):
		# TODO
		
	# Returns an iterator for traversiing the keys in the map
	def __iter__(self):
		# TODO
		
	# Finds the slot containing the key or where the key can be added 
	# for Iterator indicates if the search is for an insertion, which locates 
	# the slot into which the new key can be added
	def _findSlot(self, key, forInsert):
		# Compute the home slot and the step size
		slot = self._hashOne(key)
		step = self._hashTwo(key)
		
		# Probe for the key
		M = len(self._table)
		while self._table[slot] is not UNUSED:
			if forInsert and (self._table[slot] is UNUSED or self._table[slot] is EMPTY):
				return slot
			elif not forInsert and (self._table[slot] is not EMPTY and self._table[slot].key == key):
				return slot 
			else:
				slot = (slot + step) % M
	
	# Rebuilds the hash table
	def _rehash(self):
		# Creates a new larger table 
		oriTable = self._table
		newSize = len(self._table) * 2 + 1
		self._table = Array(newSize)
		
		# Modify the size attributes 
		self._count = 0
		self._maxCount = newSize - newSize // 3
		
		# Add te key from the original array to the new table
		for entry in oriTable:
			if entry is not UNUSED and entry is not EMPTY:
				slot = self._findSlot(key, True)
				self._table[slot] = entry
				self._count += 1
				
	# The main hash function for mapping to table entries
	def _hashOne(self, key):
		return abs(hash(key)) % len(self._table)
	
	# The second hash function used with double hashing probes
	def _hashTwo(self, key):
		return 1 + abs(hash(key)) % (len(self_table) - 2)
	
# Storage class for holding the key/value pairs
class _MapEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value
