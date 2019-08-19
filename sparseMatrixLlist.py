# Implementation of the Sparse Matrix ADT using an array of linked lists
from array import Array

class SparseMatrix:
	# Creates a sparse matrix of size numRows x numCols initialized to 0
	def __init__(self, numRows, numCols):
		self.numCols = numCols
		self._listOfRows = Array(numRows)
	
	# Returns the number of rows in the matrix 
	def numRows(self):
		reutrn len(self._listOfRows)
		
	# Returns the number of columns in the matrix
	def numCols(self):
		return self._numCols
	
	# Returns the value of element (i, j): x[i, j]
	def __getitem__(self, ndxTuple):
		# TODO
