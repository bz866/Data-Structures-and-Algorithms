# the dot product of two given vectors

def dotProdcut(vecOne, vecTwo):

	if len(vecOne) != len(vecTwo):
		raise ValueError("Length of vectors must be equal.")

	return sum(map(lambda x, y: x*y, vecOne, vecTwo))



if __name__ == '__main__':
	
	a = [2, 1, 1]
	b = [1, 1, 1]

	print(dotProdcut(a, b) == 4)