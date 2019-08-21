# Implementation of the bounded Priority Queue ADT using an array of 
# queues in which the queues are implemented using a linked list
from array import Array
from queuebyLinkedList import Queue

class BoundedPriorityQueue:
	# Creates an empty bounded priority queue
	def __init__(self, numLevels):
		self.qSize = 0
		self.qLevels = Array(numLevels)
		for i in range(numLevels):
			self.qLevels[i] = Queue()
