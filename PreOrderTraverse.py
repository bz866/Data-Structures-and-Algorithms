
# Leetcode 590
# Traverse in preorder
# BFS and DFS


def postOrderBFS(root):

	if not root:
		return []

	res = []
	stack = []
	stack.append(root.val)

	while len(stack) > 0:
		curNode = stack.pop(-1)
		res.append(curNode.val)

		if curNode.children:
			for child in curNode.children:
				stack.append(child)

	return res[::-1]

class Solution:
	def postOrderDFS(self, root):

		if not root:
			return []

		self.res = []
		self._postOrderTraverseDFS(root)

		return self.res

	def _postOrderTraverseDFS(self, node):

		if node.children:
			for child in node.children:
				self._postOrderTraverseDFS(child)

		self.res.append(node.val)

