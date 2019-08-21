# implementation of the Polynomial ADT using a sorted linked list
class Polynomial:
	# Create a new polynomial object
	def __init__(self, degree = None, coefficient = None):
		if degree is None:
			self._polyHead = None 
		else:
			self._polyHead = PolyTermNode(degree, coefficient)
		self._polyTail = self._polyHead
		
	# Return the degree of the polynomial
	def degree(self):
		if self._polyHead is None:
			return -1
		else:
			return self._polyHead.degree
		
	# Return the coefficient for the term of the given degree
	def __getitem__(self, degree):
		assert self.degree >= 0, "Operation not permitted on an empty polynomial."
		curNode = self._polyHead
		while curNode is not None and curNode.degree >= degree:
			curNode = curNode.next
			
		if curNode is None or curNode.degree != degree:
			return 0.0
		else:
			return curNode.degree
		
	# Evaluate the polynomial at the given scalar value
	def evaluate(self, scalar):
		assert self.degree() >= 0, "Only non-empty polynomial can be evaluated."
		result = 0.0
		curNode = self._polyHead
		while curNode is not None:
			result += curNode.coefficient * (scalar ** curNode.degree)
			curNode = curNode.next
		return result
	
	# Polynomial addition: newPoly = self + rhsMatrix
	def __add__(self, rhsPoly):
		#TODO
		
	# Polynomial substraction: newPoly = self - rhsPoly
	def __sub__(self, rhsPoly):
		#TODO
		
	# Polynomial multiplication: newPoly = self * rhsPoly
	def __mul__(self, rhsPoly):
		#TODO
	
	# Helper method for appending terms to the polynomial
	def _appendTerm(self, degree, coefficient):
		if coefficient != 0.0:
			newTerm = _PolyTermNode(degree, coefficient)
			if self._polyHead is None:
				self._polyHead = newTerm
			else:
				self._polyTail.next = newTerm
			self._polyTail = newTerm
	
# Class for creating polynomial term nodes used with the linked list
class _PolyTermNode(object):
	def __init__(self, degree, coefficient):
		self.degree = degree
		self.coefficient = coefficient 
		self.next = None
