# Implementation of common recursion sequences
# Factorial

# Compute n!
def factorial(n):
	assert n >= 0, " Factorial not defined for negative values."
	if n < 2: 
		return 1 
	else: 
		return n * fact(n-1)
	
	
# Fibonacci Sequence
# Compute the nth number in the Fibonacci Sequence in recursion
def fibonacciRec(n):
	assert n >= 0, "Fibonacci not defined for n < 0"
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
	
# yield the Fibonacci Sequence in while loop
def fibonacciWhile(n):
	assert n >= 0, "Fibonacci not defined for n < 0"
	prev = 0
	next = 1
	while n > 0:
		yield prev
		prev, next = next, prev + next
		n -= 1
		
# Print the contents of a singly linked list in reverse order
def printListBF(head):
	# Count the number of nodes in the list
	numNodes = 0
	curNode = head
	while curNode is not None:
		curNode = curNode.next
		numNodes += 1
		
		# Iterate over the linked list multiple times. The first iteration prints the last item
		# the second iteration prints the next to last item and so on
		for i in range(numNodes):
			curNode = head # The temporary pointer starts from the first node each time
			for i in range(numNodes - 1): # Iterate one less time for iteration of the outer loop
				curNode = curNode.next
				
			# print the data in the node referenced by curNode
			print(curNode.data)
			
# Print the contents of a linked list in reverse order using a stack
from lliststack import Stack

def printListStack(head):
	# Createe a stack to store the items
	s = Stack()
	# Iterate throught the list and push each item onto the stack
	curNode = head 
	while curNode is not None:
		s.push(curNode.data)
		curNode = curNode.next
		
	# Repeatedly pop the items from the stack and print them until the stack is empty
	while not s.isEmpty():
		item = s.pop()
		print item
		
# Print the contents of a linked list using recursion
def printList(node):
	if node is not None:
		printList(node.next)
		print(node.data)
		
 # Performs a recursion binary search on a sorted sequence
def recBinarySearch(target, theSeq, left, right):
	# If the sequence cannot be subdivided further, we are done
	if left > right:
		return False
	else:
		# Find the midpoint of the sequence 
		mid = (last + first) // 2
		# Does the element at the midpoint contain the target
		if theSeq[mid] == target:
			return True # found
		# go left
		elif target < theSeq[mid]:
			return recBinarySearch(target, theSeq, first, mid - 1)
		# go right
		else:
			return recBinarySearch(target, theSeq, mid + 1, last) 
		

	
