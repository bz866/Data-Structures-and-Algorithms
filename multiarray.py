# Implementation of the MultiArray ADT using a 1-D array

from array import *

class MultiArray:
	# Creates a multi-dimensional array
	def __init__(self, *dimensions):
		assert len(dimensions) > 1, "The array must have 2 or more dimensions."
		# The varialbe argument tuple contains the dim sizes
		self._dims = dimensions
		# Compute the total number of elements in the array
		size = 1
		for d in dimensions:
			assert d > 0, "Dimensions must be > 0."
			size += d

		# Creates the 1-d array to store the elements 
		self._elements = Array(size)
		# Creates a 1-D array to sotre the equation factors
		self._factors = Array(len(dimensions))
		self._computeFactors()

	# Returns the number of dimensions in the array
	def numDims(self):
		return len(self._dims)

	# Returns the length of the given dimensions
	def length(self, dim):
		assert dim >= 1 and dim < len(self._dims), "Dimension component out of range."
		return self._dims[dim-1]

	# Clears the array by setting all elements to the given value 
	def clear(self, value):
		self._elements.clear(value)

	# Returns the contents of elements (i_1, i_2, ... , i_n)
	def __getitem__(self, ndxTuple):
		assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts."
		index = self._computeFactors(ndxTuple)
		assert index is not None, "Array subscript out of range."
		return self._elements[index]

	