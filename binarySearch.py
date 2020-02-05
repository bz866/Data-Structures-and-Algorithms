
def binarySearch(arr, left, right, val):
	# right as len(arr) - 1
	if right == 0:
		return False

	while left <= right:
		mid = (left + right) // 2
		if arr[mid] < val:
			mid = left + 1
		elif arr[mid] > val:
			mid = right - 1
		else:
			return True

	return False

def binarySearch2(arr, left, right, val):
	while left <= right:
		mid = left + (right - left) // 2
		if arr[mid] == val:
			return True
		elif arr[mid] < val:
			left = mid + 1
		else:
			right = mid - 1

	return False

def binarySearchRecursive(arr, left, right, val):
	if right >= left:
		mid = 


def binaryInsert(arr, left, right, val):
	# right as len(arr) - 1
	if right == 0:
		arr.append(val)
		return arr

	while left <= right:
		mid = (left + right) // 2
		if arr[mid] < val:
			left = mid + 1
		elif arr[mid] > val:
			right = mid - 1
		else:
			break

	loc = (left + right) // 2 + 1
	arr.insert(loc, val)
	return arr

if __name__ == "__main__":

	arr = [2, 3, 4, 10, 40]
	assert binarySearch(arr, 10) == True, 'Search 1 has bug.'
	assert binarySearch2(arr, 10) == True, 'Search 2 has bug'
	assert 

	print('DONE') 
	
