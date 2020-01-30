# The minimum number of trials to see which floor breaks the egg
# DP
# In general, n eggs m floors 
# f[n][m] = 1 + max(f[n-1][k-1], f[n][m-k]), k in [1, m-1]
# Ref: https://www.cnblogs.com/grandyang/p/11048142.html
# TLE optimization needed


def countMinStep(numEggs, numFloors):
	if numEggs < 1 or numFloors < 1:
		return 0

	trials = []
	for i in range(numEggs+1):
		ls = []
		for j in range(numFloors+1):
			ls.append(j)
		trials.append(ls)

	print(trials)

	for eggInd in range(2, numEggs+1):
		for floorInd in range(1, numFloors+1):
			for k in range(1, floorInd):
				trials[eggInd][floorInd] = min( trials[eggInd][floorInd], 1+max(trials[eggInd-1][k-1], trials[eggInd][floorInd-k]) )


	return trials[numEggs][numFloors]


if __name__ == '__main__':
	
	# 2 eggs, 100 floors, trials = 14
	print(countMinStep(2, 100))
	assert countMinStep(2, 100) == 14, '2 eggs 100 floors != 14'


