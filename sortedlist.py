# Implementation of the self-sorted list
class sortedList:
	# Creates an empty list instance
	def __init__(self):
		self._theElements = list()



	# Modified version of the binary search that returns the index within 
	# a sorted sequence indicating where the target should be located
	def _findSortedPositon(self, target):
		left = 0
		right = len(self._theElements) - 1
		while left <= right:
			mid = (left + right) // 2 
			if self._theElements[mid] < target:
				left = left + 1
			elif self._theElements[mid] > target:
				right = right - 1
			else: # found 
				return mid

		return left # index where the target value should be