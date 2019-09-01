# Implementation of the radix sort using an array of queues
# Sorts a sequence of positive integers using the radix sort algorithm

from array import array
from queueByLinkedList import Queue

def radixSort(intList, numDigits):
	# Create an array of queues to represent the bins
	binArray = Array(10)
	for k in range(10):
		binArray[k] = Queue()

	# The value of the current column
	column = 1

	# Iterate over the number of digits in the largest value 
	for d in range(numDigits):
		digit = (key // column) % 10
		binArray[digit].enqueue(key)

	# Gather the keys from the bins and place them back intList
	i = 0
	for bin in binArray:
		