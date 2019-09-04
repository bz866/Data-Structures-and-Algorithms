# Preorder traversal on a binary tree
def preorderTrav(subtree):
	if subtree is not None:
		print(subtree.data)
		preorderTrav(subtree.left)
		preorderTrav(subtree.right)

# Inorder traversal on a binary tree
def inorderTrav(subtree):
	if subtree is not None:
		inorderTrav(subtree.left)
		print(subtree.data)
		inorderTrav(subtree.right)

# Postorder traversal on a binary tree
def postorderTrav(subtree):
	if subtree is not None:
		postorderTrav(subtree.left)
		postorderTrav(subtree.right)
		print(subtree.data)

# Breath-first traversal on a binary tree
import queue
def breadthFirstTrav(bintree):
	# Create a empty queue add the root node to it
	q = queue.Queue()
	q.enqueue(bintree)

	# Visit each node in the tree
	while not q.isEmpty():
		# remove the next node from the queue and visit it
		node = q.dequeue()
		print(node.data)

		# Add the two children to the queue
		if node.left is not None:
			q.enqueue(node.left)
		if node.right is not None:
			q.enqueue(node.right)

# 