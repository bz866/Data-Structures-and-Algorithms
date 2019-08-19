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
		rowNdx = ndxTuple[0]
		colNdx = ndxTuple[1]
		preNode = None 
		curNode = self._listOfRows[rowNdx]
		while (curNode is not None and curNode.col != col):
			preNode = curNode
			curNode = curNode.next
		
		# See if the element is in the list
		if curNode is not None and curNode.col == col: # the element in the linked list
			return curNode.value
		else: # not in the linked list
			return 0.0
	
	# Sets the value of element (i, j) to the value s: x[i, j] = s
	def __setitem__(self, ndxTuple, value):
		rowNdx = ndxTuple[0]
		colNdx = ndxTuple[1]
		preNode = None
		curNode = self._listOfRows[rowNdx]
		while (curNode is not None and curNode.col != col):
			preNode = curNode
			curNode = curNode.next
			
		# see if the element is in the list 
		if curNode is not None and curNode.col == col:
			if value == 0.0: # remove the element
				if curNode == self._listOfRows[row]: # target element is the head node of a row(each row is a linked list)
					self._listOfRows[row] = curNode.next
				else: # target element is in the middle of a row
					preNode.next = curNode.next
			elif value != 0.0: # add the element into the row (linked list)
				newNode = _MatrixElementNode(col, value)
				newNode.next = curNode
				if curNode == self._listOfRows[row]: # add to the head of the row
					self._listOfRows[row] = curNode
				else: # add to the middle or the end of the row
					preNode.next = newNode
	
	# Scales the matrix by given scalar
	def scaleBy(self, scalar):
		for row in range(0, len(self._listOfRows)):
			curNode = self._listOfRows[row]
			while curNode is not None:
				curNode.value *= scalar
				curNode = curNode.next
				
	# Creates and returns a new Matrix that is the transpose of this matrix
	def transpose(self):
		
	# Matrix addition: newMatrix = self + rhsMatrix
	def __add__(self, rhsMatrix):
		assert self.numCols() == rhsMatrix.numCols(), "Matrix columns not compatable for adding."
		assert self.numRows() == rhsMatrix.numRows(), "Matrix rows not compatable for adding."
		
		newMatrix = SparseMatrix(self.numRows(), self.numCols) # Create a new sparse matrix of the same size
		for row in range(0, len(self.numRows()):
			curNode = self._listOfRows[row]
			while curNode is not None:
				newMatrix[row, curNode.col] = curNode.value # __setitem__()
				curNode = curNode.next
		
		for row in range(0, len(self.numRows()):
			curNode = rhsMatrix._listOfRows[row]
			while curNode is not None:
# 				value = newMatrix[row, curNode.col]
# 				value += curNode.value
# 				newMatrix[row, curNode.col]  = value
				newMatrix[row, curNode.col] += curNode.value
				curNode = curNode.next
						 
		return newMatrix
	
	def __sub__(self, rhsMatrix):
		assert self.numCols() == rhsMatrix.numCols(), "Matrix columns not compatable for subbing."
		assert self.numRows() == rhsMatrix.numRows(), "Matrix rows not compatable for subbing."
						 
		newMatrix = SparseMatrix(self.numRows(), self.numCols) # Create a new sparse matrix of the same size
		for row in range(0, len(self.numRows()):
			curNode = self._listOfRows[row]
			while curNode is not None:
				newMatrix[row, curNode.col] = curNode.value # __setitem__()
				curNode = curNode.next
						 
		for row in range(0, len(self.numRows()):
			curNode = rhsMatrix._listOfRows[row]
			while curNode is not None:
# 				value = newMatrix[row, curNode.col]
# 				value += curNode.value
# 				newMatrix[row, curNode.col]  = value
				newMatrix[row, curNode.col] -= curNode.value
				curNode = curNode.next
		
		return newMatrix
						 
	def __mul__(self, rhsMatrix):
		assert self.numCols() == rhsMatrix.numRows() and \
			   self.numRows() == rhsMatrix.numCols(), "Matrix sizes not compatable for multiplying."
			

# Storage class for creating matrix element nodes
class _MatrixElementNode:
	def __init__(self, col, value):
		self.col = col
		self.value = value
		self.next = None
