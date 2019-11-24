# GCD Groups Programming Practice

def gcd(numOne, numTwo):
	"""
	Useless when b == 0
	the result will have the same sign as b (so that when b is divided by it, the result comes out positive)
	"""
	while numTwo:
		numOne, numTwo = numTwo, (numOne % numTwo)
	return numOne

def hasGCDGroups(arr):
	
	if len(arr) < 2:
		return False

	n = len(arr)
	firstArr = []
	secondArr = []

	GCDFirstArr = None
	GCDSecondArr = None

	for val in arr:

		if val == 1:
			return False

		if len(firstArr) == 0:
			firstArr.append(val)
			GCDFirstArr = val
			continue

		print("INCOMING RESULT: {} || {}".format(firstArr, secondArr))

		tmpGCD = gcd(GCDFirstArr, val)
		if tmpGCD != 1:
			GCDFirstArr = tmpGCD
			firstArr.append(val)
		else:
			if len(secondArr) == 0:
				secondArr.append(val)
				GCDSecondArr = val
				continue
			else:
				tmpGCD = gcd(GCDSecondArr, val)
				if tmpGCD!= 1:
					GCDSecondArr = tmpGCD
					secondArr.append(val)
				else:
					return False

	print("STAGE RESULT: {} || {}".format(firstArr, secondArr))

	if len(firstArr) == len(secondArr):
		return True
	else: # balance two array
		if len(secondArr) == 0:
			firstArr, secondArr = firstArr[0: (n//2)], firstArr[n//2 :]
			print("STAGE RESULT: {} || {}".format(firstArr, secondArr))
			return True

		ind = 0
		while len(firstArr) != len(secondArr):
			curVal = firstArr[ind]
			tmpGCD = gcd(GCDSecondArr, curVal)
			if tmpGCD != 1:
				secondArr.append(firstArr.pop(ind))
				GCDSecondArr = tmpGCD
			else:
				ind += 1

			if len(firstArr) == len(secondArr):
				break

	print("SPLIT RESULT: {} || {}".format(firstArr, secondArr))
	return len(firstArr) == len(secondArr)

if __name__ == "__main__":
	
	sample = [8, 10, 24, 20, 45, 30]
	print(hasGCDGroups(sample))	

	sample = [25, 1]
	print(hasGCDGroups(sample))

	sample = [i for i in range(2, 18, 2)]
	print(hasGCDGroups(sample))


