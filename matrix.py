# Implementation of the Matrix ADT using a 2-D array
from array import Array
from array2D import Array2D

class Matrix:
	# Create a matrix of size numRows * numCols initialized to 0
	def __init__(self, numRows, numCols):
		assert numRows >= 0 and numCols >= 0, "The matrix must have numRows >= 0 and numCols >= 0."
		self._theGrid = Array2D(numRows, numCols)
		self._theGrid.clear(0) # initialize with all zeros

	# Return the number of rows in the matrix
	def numRows(self):
		return self._theGrid.numRows()

	# Return the number of columns in the matrix
	def numCols(self):
		return self._theGrid.numCols()

	# Returns the value of element (i ,j): x[i, j]
	def __getitem__(self, ndxTuple):
		return self._theGrid(ndxTuple[0], ndxTuple[1])

	# Set the value of element (i, j) to the value s: x[i, j] = s
	def __setitem__(self, ndxTuple, value):
		self._theGrid[ndxTuple[0], ndxTuple[1]] = value

	# Scales the matrix by the given scalar value 
	def scaleBy(self, valueToScalar):
		for i in range(0, self._theGrid.numRows):
			for j in range(0, self._theGrid.numCols):
				self._theGrid[i, j] += valueToScalar

	# Creates and returns a new matrix that is the transpose of this matrix
	def transpose(self):
		newMatrix = Matrix(numCols, numRows)
		for rowIdx in range(0, self._theGrid.numRows()):
			for colIdx in range(0, self._theGrid.numCols()):
				newMatrix[colIdx, rowIdx] = self[rowIdx, colIdx]
		return newMatrixr

	# Creates and returns a new matrix that results from matrix addition
	def __add__(self, rhsMatrix):
		assert rhsMatrix.numRows() == self._theGrid.numRows(), "Matrix number of rows not compatible for the add operation."
		assert rhsMatrix.numCols() == self._theGrid.numCols(), "Matrix number of columns not compatible for the add operation."
		newMatrix = Matrix(self.numRows, self.numCols)
		for rowIdx in range(0, self,numRows):
			for colIdx in range(0, self.numCols):
				newMatrix[rowIdx, colIdx] = self[rowIdx, colIdx] + rhsMatrix[rowIdx, colIdx] # add
		return newMatrix


	def __sub__(self, rhsMatrix):
		assert rhsMatrix.numRows() == self._theGrid.numRows(), "Matrix number of rows not compatible for the sub operation."
		assert rhsMatrix.numCols() == self._theGrid.numCols(), "Matrix number of columns not compatible for the sub operation."
		newMatrix = Matrix(self.numRows, self.numCols)
		for rowIdx in range(0, self,numRows):
			for colIdx in range(0, self.numCols):
				newMatrix[rowIdx, colIdx] = self[rowIdx, colIdx] - rhsMatrix[rowIdx, colIdx] # sub
		return newMatrix

	def __mul__(self, rhsMatrix):
		assert rhsMatrix.numRows() == self._theGrid.numCols(), "Matrix sizes not compatible for the mul operation."
		assert rhsMatrix.numCols() == self._theGrid.numRows(), "Matrix sizes not compatible for the mul operation."
		newMatrix = Matrix(self.numRows(), rhsMatrix.numCols())
		for rowIdx in range(0, self.numRows()):
			for colIdx in range(0, self.numCols()):
				newMatrix[rowIdx, colIdx] = [sum(self[rowIdx, i] * rhsMatrix[i, colIdx]) for i in range(0, self.numRows())][0]
		return newMatrix
