
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

	mid = (left + right) // 2 + 1
	arr.insert(mid, val)
	return arr

if __name__ == "__main__":

	
