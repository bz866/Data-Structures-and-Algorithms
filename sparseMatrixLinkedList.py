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
		curNode = self._listOfRows[rowNdx]
		while curNode is not None and curNode.col != col:
			curNode = curNode.next
		
		# check if the element in the list, if in, get it, if not, return 0.0
		if curNode is not None and curNode.col == col: # if the node exists
			return curNode.value
		elif curNode is None: # if the node doesn't exist, return 0.0 by the definition of a sparse matrix
			return 0.0
		
	# Sets the value of element (i, j) to the value s: x[i,j] = s
	def __setitem__(self, ndxTuple, value):
		rowNdx = ndxTuple[0]
		colNdx = ndxTuple[1]
		preNode = None
		curNode = self._listOfRows[row]
		while curNode is not None and curNode.col != col:
			preNode = curNode 
			curNode = curNode.next
			
		# check if the element in the list, if in, modify it, if not, add a newNode for the new value
		if curNode is not None and curNode.col == col: # if the node exist
			if value == 0.0: # remove the node
				if curNode == self._listOfRows[row]: # if the node to remove is the head of a row
					self._listOfRow[row] = curNode.next
				else: # the node to remove is not the head of a row
					preNode.next = curNode.next
			else: # modify the node
				curNode.value = value
				
		elif value !== 0.0: # if the node not exist and the value to assign is not 0.0
			newNode = _MatrixElementNode(col, value)
			newNode.next = curNode
			if curNode == self._listOfRows[row]: # 
				self._listOfRows[row] = newNode
			else:
				preNode.next = newNode
				
		else: # the value to assign is 0.0, by the definition of the sparse matrix, we only store nodes with non-zero values
			pass 
		
	# Scales the matrix by the given scalar
	def scaleBy(self, scalar):
		for row in range(self.numRows):
			curNode = self._listOfRows[row]
			while curNode is not None:
				curNode.value *= scalar
				curNode = curNode.next
				
	# Creates and returns a new matrix that is the transpose of this matrix
	def transpose(self):
		#TODO
		
	# Matix addition: newMatrix =  self + rhsMatrix
	def __add__(self, rhsMatrix):
		# make sure the two matrix have consistent size
		assert self.numRows() == rhsMatrix.numRows() and \
				self.numCols() == rhsMatrix.numCols(), \
				"Matrix sizes not compatable for adding."
		
		# Create a new sparse matrix of the same size
		newMatrix = SparseMatrix(self.numRows(), self.numCols())
		
		# Add the element of this matrix to the new matrix 
		for row in range(self.numRows()):
			curNode = self._listOfRows[row]
			while curNode is not None:
				newMatrix[row, curNode.col] = curNode.value
				curNode = curNode.next
		
		# Add the elements of the rhsMatrix to the new matrix
		for row in range(rhsMatrix.numRows()):
			curNode = rhsMatrix._listOfRows[row]
			while curNode is not None:
				value = newMatrix._listOfRows[row, curNode.col]
				value += curNode.value
				newMatrix._listOfRows[row, curNode.col] = value
				curNode = curNode.next

		return newMatrix
	
	# Matix subtraction: newMatrix =  self - rhsMatrix
	def __sub__(self, rhsMatrix):
		# TODO
	
	# Matrix multiplication: newMatrix = self * rhsMatrix.T
	def __mul__(self, rhsMatrix):
		# TODO

# Storage class for creating matrix element nodes
class _MatrixElementNode:
	def __init__(self, col, value):
		self.col = col
		self.value = value 
		self.next = None
