# Implementation of the quick sort algorithm
def quickSort(theList, left, right):
	# left = 0
	# right = len(theList) - 1

	if left < right:
		pi = partition(theList, left, right)

		quickSort(theList, left, pi-1)
		quickSort(theList, pi+1, right)

	return theList


def partition(arr, left, right):
	i = left - 1
	pivot = arr[right]

	for j in range(left, right):
		if arr[j] > pivot: # > descending, < ascending
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[right] = arr[right], arr[i+1]
	return i + 1

def kLargestNumber(arr, k):
	left = 0
	right = len(arr) - 1

	while True:
		pi = partition(arr, left, right)
		if pi > k-1:
			right = pi - 1
		elif pi < k-1:
			left = pi + 1
		else:
			break

	return arr[pi]

if __name__ == "__main__":

	seq = [1,5,8,2,50,3937,9,0,83,8]
	print(quickSort(seq, 0, len(seq)-1))

	seq = [1,5,8,2,50,3937,9,0,83,8]
	assert kLargestNumber(seq, 2) == 83, "Klargest fail"
	print("DONE")

	