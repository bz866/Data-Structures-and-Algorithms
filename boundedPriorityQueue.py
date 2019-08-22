# Implementation of the bounded Priority Queue ADT using an array of 
# queues in which the queues are implemented using a linked list
from array import Array
from queuebyLinkedList import Queue

class BoundedPriorityQueue:
	# Creates an empty bounded priority queue
	def __init__(self, numLevels):
		self._qSize = 0
		self._qLevels = Array(numLevels)
		# The largetest number as the hignest priority
		for i in range(numLevels):
			self._qLevels[i] = Queue()

	# Returs True if the queue is empty
	def isEmpty(self):
		return self._qLevels == 0

	# Returns the number of items in the queue
	def __len__(self):
		return self._qSize

	# Adds the given item to the queue
	def enqueue(self, item, priority):
		assert priority >= 0 and priority < len(self._qLevels), "Invalid priority level"
		self._qLevels[priority].enqueue(item)

	# Removes and returns the next item in the queue
	def dequeue(self):
		# Make usre the queue is not empty
		assert not self.isEmpty(), "Cannot dequeue from an empty queue."
		# Find the first non-empty queue
		i = 0
		p = len(self._qLevels)
		while i < p and not self._qLevels[i].isEmpty():
			i += 1
		# We know the queue is not empty, so dequeue from the ith queue
		return self._qLevels[i].dequeue() 

	
