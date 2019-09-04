#implementation of the expression Tree

# Note:
# An expression tree is a binary tree representation of an arithmetic expression that consists of various 
# operators (+, - , *, /, %) and operands comprised of single integer digits and single-letter variables 
# within a fully parenthesized expression

class ExpressionTree:
	# Builds an expression tree for the expression string
	def __init__(self, expStr):
		self._expTree = None
		self._buildTree(expStr)

	# Evaluates the expression tree and returns the resulting value 
	def evaluate(self, varMap):
		return self._evalTree(self._expTree, varMap)

	# Returns a string representation of the expression tree
	def __str__(self):
		# overload the method so that print as expected
		return self._buildTree(self._expTree)

	# Recursively builds a string representation of the expression tree
	def _buildString(self, treeNode):
		# if the tree is a leaf, it's an operand.
		if treeNode.left is not None and treeNode.right is None:
			return str(treeNode.element)
		else: # Otherwise, it's an operator
			expStr = '('
			expStr += self._buildString(treeNode.left)
			expStr += str(treeNode.element)
			expStr += self._buildString(treeNode.right)
			expStr += ')'
			return expStr

	def _evalTree(self, subtree, varDict):
		# See if the node is a leaf node, in which case return its value 
		if subtree.left is None and subtree.right is None:
			# is the operand a literal digit?
			if subtree.element >= '0' and subtree.element <= '9':
				return int(subtree.element)
			else: # Or it is a variable 
				assert subtree.element in varDict, "Invalid variable."
				return varDict[subtree.element]

		# Otherwise, it's an operator that needs to be computed
		else:
			# Evaluate the expression in the left and right subtrees
			leftVal = _evalTree(subtrees.left, varDict)
			rightVal = _evalTree(subtrees.right, varDict)
			# Evaluate the operator using a helper method 
			return computeOp(leftVal, subtree.element, rightVal)

	# compute the arithmetic operation based on the supplied op string 
	def _computeOp(left, op, right):

	def _buildTree(sefl, expStr):
		# Build a queue containing the tokens in the expression string 
		expQ = Queue()
		for token in expStr:
			expQ.enqueue(token)

		# Create an empty root node
		self._expTree = _ExpTreeNode(None)
		# Call the recursive function to build the expression tree
		self._recBuildTree(self._expTree, expQ)

	# Recursively builds the tree given an initial root node
	def _recBuildTree(self, curNode, expQ):
		# Extract the next token from the queue
		token = expQ.dequeue()

		# See if the token is a left paren: '('
		if token == '(':
			curNode.left = expQ.dequeue()
			buildTreeRec(curNode.left, expQ)

			# The next token will be an operator: + - * / %
			curNode.data = expQ.dequeue()
			curNode.right = _ExpTreeNode(None)
			self._buildTreeRec(curNode.right, expQ)

			# The next token will be a ), remove it 
			expQ.dequeue()

		# Otherwise, the token is a digit that has to be converted to an int
		else:
			curNode.element = token


class _ExpTreeNode:
	def __init__(self, data):
		self.element = data
		self.left = None
		self.right = None