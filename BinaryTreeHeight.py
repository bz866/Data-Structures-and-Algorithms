
# Get the height of a binary tree

def height(node):
  if not node:
    return 0
  
  # Recursive to get the height of subtrees
  # Backtrack to record
  if node.left:
    leftHeight = height(node.left)
  if node.right:
    rightHeight = height(node.right)
    
  # dynamically to record the deeper side
  if leftHeight > rightHeight:
    return leftHeight + 1
  else:
    return rightHeight + 1
