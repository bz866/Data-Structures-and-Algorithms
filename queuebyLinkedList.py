# Implementation of the Queue ADT using a linked list
class Queue:
	# Creates an empty queue
	def __init__(self):
		self._qHead = None 
		self._qTail = None
		self._size = 0
		
	# Returns True if the queue is empty
	def isEmpty(self):
		return self._qHead is None and self._qTail is None and self._size == 0
	
	# Returns the number of items in the queue
	def __len__(self):
		return self._size
	
	# Adds the given item to the queue
	def enqueue(self, item):
		newNode = _QueueNode(item)
		if self._qHead is None: # empty queue add item
			self._qHead = newNode
			self._qTail = newNode
		else: # non-empty queue add item
			self._qTail.next = newNode
			self._qTail = newNode
			
		self._size += 1
		
	# Removes and returns the first item in the Queue
	def dequeue(self):
		assert not self.isEmpty(), "Cannot dequeue from an empty queue."
		node = self._qHead
		if self._qHead is self._qTail:
			self._qTail = None
		self._qHead = self.qHead.next
		self._size -= 1
		return node.item	
			
# Private Storage class for creating the linked list nodes
class _QueueNode(object):
	def __init__(self, item):
		self.item = item
		self.next = None
