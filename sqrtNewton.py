# a sqrt function without using built in functions

def sqrtNewton(target, x0, numIter):

	xNew = x0
	diff = target - xNew**2

	for i in range(0, numIter):
		xNew = iterToUpdate(target, xNew)
		diff = target - xNew**2
		if diff == 0:
			break
		print("{:.8f}->{:.8f}".format(xNew, target))

	return xNew


def iterToUpdate(target, x):

	return x - (target - x**2) / (-2 * x)



if __name__ == "__main__":

	target = 2.0
	x0 = 2.0
	res = sqrtNewton(target, x0, 500)

	print("Result: {:.10f}".format(res))
	print("Sqaure: {:.10f}".format(res**2))