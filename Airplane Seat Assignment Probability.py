# recursively

def nthPersonGetsNthSeatRecursively(n: int) -> float:
	if n == 1:
		return 1.0

	probRight = 1 / n * 1 # land on the person's right seat
	probRand = (n - 2) / n * nthPersonGetsNthSeatRecursively(n-1) # land randomly, either the person's seat or my seat 
	probMySeat = 1 / n * 0 # land on my seat

	return probRight + probRand + probMySeat

# DP
def nthPersonGetsNthSeatDP(n: int) -> float:
	if n == 1:
		return 1.0

	prev = 1.0
	for i in range(2, n):
		cur = 1 / i + (i - 2) / i * prev
		prev = cur

	return prev

# def nthPersonGetsNthSeatDP(n: int) -> float:


if __name__ == '__main__':
	
	assert nthPersonGetsNthSeatRecursively(1) == 1.000, '1 case wrong'
	assert nthPersonGetsNthSeatRecursively(10) == 0.500, '10 case wrong'

	assert nthPersonGetsNthSeatDP(1) == 1.000, '1 case wrong'
	assert nthPersonGetsNthSeatDP(100) == 0.500, '100 case wrong'
	assert nthPersonGetsNthSeatDP(100000) == 0.500, '100000 case wrong'

	print("DONE!")