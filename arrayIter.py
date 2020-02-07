
class Array:
	def __init__(self, nums):

		self.__nums = nums

	def __len__(self):
		return len(self.__nums)

	def __getitem__(self, idx):
		return self.__nums[idx]

	def __setitem__(self, idx, value):
		self.__nums[idx] = value

	def __iter__(self):
		return _ArrayIterator(self.__nums)

	def __str__(self): # the method must return String object
		return "A self-defined array to test __str__()"

	def __repr__(self): # if __str__ not defined, print an object will return the content from __repr__()
		return "sample __repr__" 

class _ArrayIterator:
	def __init__(self, nums):
		self.__iterVals = nums
		self.__curIdx = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.__curIdx < len(self.__iterVals):
			val = self.__iterVals[ self.__curIdx ]
			self.__curIdx += 1
			return val
		else:
			raise StopIteration

if __name__ == "__main__":

	ls = list(range(0,5))
	arr = Array(ls)
	arrIter = _ArrayIterator(arr)

	print(arr) # get content in __str__()

	print(arr.__repr__()) 

	while True:
		print(next(arrIter))
		# Should get StopIteration after printing 1,2,3,4,5



