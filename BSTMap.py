# Implementation of the Map ADT using a binary search tree
class BSTMap:
	# Creates an empty map instance
	def __init__(self):
		self._root = None
		self._size = 0

	# Returns the number of entries in the map
	def __len__(self):
		return self._size

	# Returns an iterator for traversing the keys in the map
	def __iter__(self):
		return _BSTMapIterator(self._root)

	# Determines if the map contains the given key
	def __contains__(self, key):
		return self._bstSearch(self._root, key) is not None

	# Returns the value associated with the key
	def valueOf(self, key):
		node = self._bstSearch(self._root, key)
		assert node is not None , "Invalid map key."
		return node.value

	# Helper method that recursively searches the tree for a target key
	def _bstSearch(self, subtree, target):
		if subtree is None: # base case
			return None
		elif target < subtree.key: # target is left of the subtree root 
			return self._bstSearch(subtree.left)
		elif target > subtree.key: # target is right of the subtree root
			return self._bstSearch(subtree.right)
		else:
			return subtree

	# Adds a new entry to the map or replaces the value of an existing array
	def add(self, key, value):
		# Find the node containing the key, if it exists
		node = self._bstSearch(key)
		# If the key is already in the tree, update its value
		if node is not None:
			node.value = value
			return False
		# Otherwise, add a new entry
	else:
		self._root = self._bstInsert(self._root, key, value)
		self._size += 1
		return True

	# Removes the map entry associated with the given key
	def remove(self, key):
		assert key in self, "Invalid map key."
		self._root = self._bstRemove(self._root, key)
		self._size -= 1

	# Helper method that inserts a new item, recursively
	def _bstSearch(self, subtree, key, value):
		if subtree is None:
			subtree = _BSTMapNode(key, value)
		elif key < subtree.key:
			subtree.left = self._bstInsert(subtree.left, key, value)
		elif key > subtree.key:
			subtree.right = self._bstInsert(subtree.right, key, value)
		return subtree

	# helper method for finding the node containing the minimum key
	def _bstMinimum(self, subtree):
		if subtree is None:
			return None
		elif subtree.left is None:
			return subtree
		else:
			return self._bstMinimum(subtree.left) 

	# helper method that removes an existing item recursively
	def _bstRemove(self, subtree, target):
		# search for the item in the tree
		if subtree is None:
			return subtree
		elif target < subtree.key:
			subtree.left = self.._bstRemove(subtree.left, target)
			return subtree
		elif target > subtree.key:
			subtree.right = self._bstRemove(subtree.right, target)
			return subtree
		# We found the node containing the item
		else:
			if subtree.left is None and subtree.right is None:
				return None
			elif subtree.left is None or subtree.right is None:
				if subtree.left is not None:
					return subtree.left
				else:
					return subtree.right
			else:
				successor = self._bstMinimum(subtree.right)
				subtree.key = successor.key
				subtree.value = successor.value
				subtree.right = self._bstRemove(subtree.right, successor.key)
				return subtree

# An iterator for the bianry search tree using a software stack
class _BSTMapIterator:
	def __init__(self, root):
		# Creates a stack for use in traversing the tree
		self._theStack = Stack() # Stack() not imported yet
		# traverse down to the node containing the smallest key
		# during which each node along the path is pushed onto the stack
		self._traverseToMiniNode(root)

	def __iter__(self):
		return self

	# Returns the next item from the BST in the key order
	def __next__(self):
		# If the stack is empty, we are done
		if self._theStack.isEmpty():
			raise StopIteration
		else:
			# The top node on the stack contains the next key
			node = self._theStack.pop()
			key = node.key
			# If this node has a subtree rooted as the right child. we must find the node in that subtree that contains the smallest
			# key. Again, the nodes along the path are pushed onto the stack
			if node.right is not None:
				self._traverseToMiniNode(node.right)

	# Traverse down the subtreet to find the node containing the smallest key during which the nodes along that path are pushed onto the stack
	def _traverseToMinNode(self, subtree):
		if subtree is not None:
			self._theStack.push(subtree)
			self._traverseToMinNode(subtree.left)

# # An iterator for the binary search tree using the array
# class _BSTMapIterator:
# 	def __init__(self, root, size):
# 		# Creates the array and fills it with the keys
# 		self._theKeys = Array(size)
# 		self._curItem = 0 # Keep track of the next location in the array
# 		self._bstTravesal(root)
# 		self._curItem = 0 # Reset the current item index

# 	def __iter__(self):
# 		return self

# 	# Returns the next key from the array of keys
# 	def __next__(self):
# 		if self._curItem < len(self._theKeys):
# 			key = self._theKeys[self._curItem]
# 			self._curItem += 1
# 			return key
# 		else:
# 			raise StopIteration

# 	# Performs an inorder traversal used to build the array of keys
# 	def _bstTravesal(self, subtree):
# 		if subtree is not None:
# 			self._bstTravesal(subtree.left)
# 			self._theKeys[self._curItem] = subtree.key
# 			self._curItem += 1
# 			self._bstTravesal(subtree.right)

# Storage class for the binary search tree nodes of the map
class _BSTMapNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value 
		self.left = None
		self.right = None