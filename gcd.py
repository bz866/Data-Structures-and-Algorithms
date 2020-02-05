
def gcdOneNaive(numOne, numTwo):
	if numOne == 0 or numTwo == 0:
		raise ValueError("No ways to calculate the greatest common divisor for 0")

	if numOne > numTwo:
		small = numTwo
	else:
		small = numOne

	gcd = 1
	for i in range(1, small+1):
		if (numOne % i == 0) and (numTwo % i == 0):
			gcd = i

	return gcd 


def gcdTwo(numOne, numTwo):
	if numOne == 0 or numTwo == 0:
		raise ValueError("No ways to calculate the greatest commmon divisor for 0")

	while numTwo:
		numOne, numTwo = numTwo, numOne % numTwo
	return numOne


if __name__ == '__main__':
	
	assert gcdOneNaive(80, 44) == 4, "1 error"
	assert gcdOneNaive(57, 49) == 1, "2 error"

	assert gcdTwo(80, 44) == 4, "3 error"
	assert gcdTwo(57, 49) == 1, "4 error"

	print("DONE")