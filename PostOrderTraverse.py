
# Leetcode 589
# Traverse N-ary tree in PreOrder

def preOrderBFS(root):

	if not root:
		return []

	res = []
	stack = []
	stack.append(root)

	while len(stack) > 0:
		curNode = stack.pop(-1)
		res.append(curNode.val)

		if curNode.children:
			for i in range(len(curNode.children)-1, -1, -1):
				stack.append(curNode.children[i])

	return res

class Solution:
	def preOrderDFS(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        
        self.res = []
        self._dfs(root)
        
        return self.res
        
    def _dfs(self, node):
        
        self.res.append(node.val)
        
        if node.children:
            for child in node.children:
                self._dfs(child)