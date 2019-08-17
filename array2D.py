# Implementation of the Array2D ADT using an array of arrays

from array import *

class Array2D:
	# Creates a 2-D array of size numRows * numCols 
	def __init__(self, numRows, numCols):
		# Create a 1-D array to store an array reference for each row
		self._theRows = Array(numRows)

		# Create a 1-D array for each row of the 2-D array
		for i in range(0, numRows): 
			self._theRows[i] = Array(numCols)

	# Returns the number of rows in the 2-D array
	def numRows(self):
		return len(self._theRows)

	# Returns the number of columns in the 2-D array
	def numCols(self):
		return len(self._theRows[0])

	# Clears the array by setting every element to the given value 
	def clear(self, value):
		for i in range(0, len(self._theRows)):
			self._theRows[i].clear(value)

	# Gets the contents of the element at position [1, 1]
	def __getitem__(self, ndxTuple)
		assert len(ndxTuple) == 2, "Invalid number of array subscripts."
		row = ndxTuple[0]
		col = ndxTuple[1]
		assert 0 <= row and row < self.numRows(), "Array row subscript out of range."
		assert 0 <= col and col < self.numCols(), "Array column subscript out of range."
		
		return self._theRows[row][col] # access and return 

	# Sets the contents of the element at position [i, j] to value 
	def __setitem__(self, ndxTuple, value)
		assert len(ndxTuple) == 2, "Invalid number of array subscripts."
		row = ndxTuple[0]
		col = ndxTuple[1]
		assert 0 <= row and row < self.numRows(), "Array row subscript out of range."
		assert 0 <= col and col < self.numCols(), "Array column subscript out of range."

		self._theRows[row][col] = value # access and modify