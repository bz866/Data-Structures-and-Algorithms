
def inOrderBFSOne(root):
  res = []
  stack = []
  curNode = root
  
  while len(stack) > 0 or curNode:
    if curNode:
      stack.append(curNode)
      curNode = curNode.left
      continue
    curNode = stack.pop(-1)
    res.append(curNode.val)
    curNode = curNode.right
    
  return res

def inOrderBFSTwo(root):
  res = []
  stack = []
  curNode = root
  
  while len(stack) > 0 or curNode:
    while curNode:
      stack.append(curNode)
      curNode = curNode.left
    curNode = stack.pop(-1)
    res.append(curNode.val)
    curNode = curNode.right
    
  return res

  




def Solution:
  def inOrderTraverse(self, root):
    if not root:
      return []
      
    self.res = []
    self._dfs(root)
    
    return self.res
    
    
  def _dfs(self, node):
    if not node:
      return
    self._dfs(node.left)
    self.res.append(node.val)
    self._dfs(node.right)
