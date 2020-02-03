
def func(x, decimal):
	return round(x**3 + x**2 - 3 * x + 1, decimal)

def bisectionOptimization(left, right, target, tol=0.0001):
	# make sure that:
	# func(left) < 0 && func(right) > 0
	# left can be larger than right
	
	diff = float('inf')
	while abs(diff) > tol:
		mid = (left + right) / 2
		diff = func(mid, 8)-target
		if diff > 0:
			right = mid
		elif diff < 0:
			left = mid
		else:
			break

		print(diff, mid)

	return mid



if __name__ == '__main__':
	
	print(bisectionOptimization(0.45, 0.40, 0, tol=0.0001))
