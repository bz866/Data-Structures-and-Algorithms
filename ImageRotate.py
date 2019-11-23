# Clock wise rotate a matrix 
# matrix: List[List[int]]

def rotate(matrix):
    n = len(matrix)

    for i in range(0, n//2+1):
        for j in range(i, n-i-1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n-j-1][i]
            matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
            matrix[j][n-i-1] = tmp

    return matrix


# Test
if __name__ == "__main__":

	matrix = [
			  [ 5, 1, 9,11],
			  [ 2, 4, 8,10],
			  [13, 3, 6, 7],
			  [15,14,12,16]
			 ]

	ref = [
		  [15,13, 2, 5],
		  [14, 3, 4, 1],
		  [12, 6, 8, 9],
		  [16, 7,10,11]
		]

	matrix = rotate(matrix)

	if matrix != ref:
		raise Exception('not equal')

	for row in matrix:
		print(row)

