# Implements the Bag ADT using a single linked list 
class Bag:
	# Construct and empty bag
	def __init__(self):
		self._head = None 
		self._size = 0
		
	# Returns the number of items in the bag
	def __len__(self):
		return self._size
	
	# Determines if an item is contained in the bag
	def __contains__(self, target):
		curNode = self._head
		while (curNode is not None and curNode.item != target):
			curNode = curNode.next
		return curNode is not None 
	
	# Adds a new item to the bag, add to the head of the linked lisk 
	def addToHead(self, item):
		newNode = _BagListNode(item)
		newNode.next = self._head
		self._head = newNode
		self._size += 1
		
	# Removes an instance of the item from the bag
	def remove(self, item):
		preNode = None 
		curNode = self._head
		while (curNode is not None and curNode.item != item):
			preNode = curNode 
			curNode = curNode.next
			
		# The item to remove has to be in the bag
		assert curNode is None, "The item to be removed has to be in the linked list bag."
		
		# Unlink the node and return the node
		self._size -= 1
		if curNode = self._head:
			self._head = curNode.next
		else:
			preNode.next = curNode.next
		
		return curNode.item
	
	# Returns an iterator for traversing the list of items
	def __iter__(self):
		return _LinkedListBagIterator(self._head)
	
# Defines a private storage class for creating list nodes
class _BagListNode(object):
	def __init__(self, item):
		self.item = item
		self.next = None
		
# Defines a linked iterator for the Linked List Bag ADT
class _LinkedListBagIterator:
	def __init__(self, theHead):
		self._curNode = theHead
		
	def __iter__(self):
		return self
	
	def __next__(self):
		if self._curNode is None:
			raise StopIteration
		else:
			item = self._curNode.item
			self._curNode = self._curNode.next
			return item
