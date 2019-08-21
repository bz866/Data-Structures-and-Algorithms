# Implementation of the Sparse Matrix ADT using an array of linked list
from array import array

class sparseMatrixLinkedList:
	# Creates a sparse matrix of size numRows * numCols initialized to 0
	def __init__(self, numRows, numCols):
		self._numCols = numCols
		self._listOfRows = Array(numRows)

	# Returns the number of rows in the matrix
	def numRows(self):
		return len(self._listOfRows)

	#  Returns the number of columns in the matrix 
	def numCols(self):
		return self._numCols

	# Returns the value of element (i, j): x[i, j]
	def __getitem__(self, ndxTuple):
		rowNdx = ndxTuple[0]
		colNdx = ndxTuple[1]
		row = self._listOfRows[rowNdx]
		



# Storage class for creating matrix element nodes
class _MatrixElementNode:
	def __init__(self, col, value):
		self.col = col
		self.value = value 
		self.next = None