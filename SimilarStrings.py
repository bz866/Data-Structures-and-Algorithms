# Compare two strings from two arrays of n strings and print 'yes' if they are almost similar
# and 'no' if they are not 

"""
E.g.

1- 'aaabbb'
2- 'aabb'

1- {a:3, b:3}
2- {a:2, b:2}

then a: 3-2 = 1 
and 
b: 3-2 = 1 such difference is less than 3 
Then it is similar return True

empty strings are not allowed, always False
"""

def similarStrings(strA, strB):

	if not strA or not strB:
		return False

	charCntMapA = dict()
	charCntMapB = dict()
	keysUnionSet = set()
	diff = 0

	for c in strA:
		cnt = charCntMapA.setdefault(c, 0) + 1
		charCntMapA[c] = cnt
		keysUnionSet.add(c)

	for c in strB:
		cnt = charCntMapB.setdefault(c, 0) + 1
		charCntMapB[c] = cnt
		keysUnionSet.add(c)

	for key in keysUnionSet:
		diff += abs( charCntMapA.setdefault(key, 0) - charCntMapB.setdefault(key, 0) )
		if diff >= 3:
			return False

	return True


if __name__ == "__main__":

	strA = 'aaabbb'
	strB = 'aabbbbbb'

	print(similarStrings(strA, strB))

