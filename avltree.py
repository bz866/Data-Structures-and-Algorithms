# Implementation of an AVL tree

# Constants for the balance factors
LEFT_HIGH = 1
EQUAL_HIGH = 0
RIGHT_HIGH = -1

# Implementation of the Map ADT using an AVL tree
class AVLMap:
	def __init__(self):
		self._root = None
		self._size = 0

	def __len__(self):
		self._size

	def __contains__(self, key):
		return self._bstSearch(self._root, key) is not None

	def add(self, key, value):
		node = self._bstSearch(key)
		if node is not None:
			node.value = value 
			return False
		else:
			(self._root, tmp) = self._avlInsert(self._root, key, value)
			self._size += 1
			return True

	def valueOf(self, key):
		node = self._bstSearch(self._root, key)
		assert node is not None, "Invalid map key."
		return node.value

	def remove(self, key):
		assert key in self, "Invalid map key."
		(self._root, tmp) = self._avlRemove(self._root, key)
		self._size -= 1

	def __iter__(self):
		return _BSTMapIterator(self._root)

	# Rotates the pivot to the right around its left child 
	def _avlRotateRight(self, pivot):
		C = pivot.left
		pivot.left = C.right
		C.right = pivot
		return C

	# Rotates the pivot to the left around its right child 
	def _avlRotateLeft(self, pivot):
		C = pivot.right
		pivot.right = C.left
		C.left = pivot
		return C

	# Helper functions used to rebalance AVL subtree
	def _avlLeftBalance(self, pivot):
		# Set L to point to the left child of the pivot
		C = pivot.left

		# See if the rebalancing is due to case 1
		if C.bfactor == LEFT_HIGH:
			pivot.bfactor = EQUAL_HIGH
			C.bfactor = EQUAL_HIGH
			pivot = _avlRotateRight(pivot)
			return pivot

		# Otherwise, a balance from the left is due to case 3
	else:
		# Change the balance factors
		if G.bfactor == LEFT_HIGH:
			pivot.bfactor = RIGHT_HIGH
			C.bfactor = EQUAL_HIGH
		elif G.bfactor == EQUAL_HIGH:
			pivot.bfactor = EQUAL_HIGH
			C.bfactor = EQUAL_HIGH
		else: # G.bfactor == RIGHT_HIGH
			pivot.bfactor = EQUAL_HIGH
			C.bfactor = LEFT_HIGH

		# All three cases set G's balance factor to equal high
		G.bfactor = EQUAL_HIGH

		# Perform the double rotation
		pivot.left = _avlRotateLeft(L)
		pivot = _avlRotateRight(pivot)
		return pivot

	# Recursive method to handle the insertion into an AVL tree. The function returns a tuple containing a reference to the root of the 
	# subtree and a boolean to indicate if the subtree grew taller
	def _avlInsert(self, subtree, key, newitem):
		# See if we have found the insertion point
		if subtree is None:
			subtree = _AVLTreeNode(key, newitem)
			taller = True

		# IS the key already in the tree
		elif key == subtree.data:
			return (subtree, False)

		# See if we need to navigate to the left
		elif key < subtree.data:
			(subtree, taller) = _avlInsert(subtree.left, key, newitem)
			# If the subtree grew taller, see if it needs rebalancing
			if taller:
				if subtree.bfactor == LEFT_HIGH:
					subtree.right = _avlLeftBalance(subtree)
					taller = False
				elif subtree.bfactor == EQUAL_HIGH:
					subtree.bfactor = LEFT_HIGH
					taller = True
				else: # RIGHT_HIGH
					subtree.bfactor = EQUAL_HIGH
					taller = False

		# Otherwise navigate to the right
		else key > subtree.data:
			(node, taller) = _avlInsert(subtree.right, key, newitem)
			# If the subtree grew taller, see if it needs rebalancing
			if taller:
				if subtree.bfactor == LEFT_HIGH:
					subtree.bfactor = EQUAL_HIGH
					taller = False
				elif subtree.bfactor == EQUAL_HIGH:
					subtree.bfactor = RIGHT_HIGH
					taller = True
				else: # RIGHT_HIGH
					subtree.right = _avlRightBalance(subtree)
					taller = False

		# return the reuslts 
		return (subtree, taller)

# Storage class for creating the AVL tree node
class _AVLMapNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value 
		self.bfactor = EQUAL_HIGH
		self.left = None
		self.right = None

