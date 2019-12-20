# a sqrt function without using built in functions

def newtonMethod(num, numIters = 500):
	x = num # initialization
	for i in range(0, numIters):
		x = optimizeFunc(num, x) # update by newton method
		
	return x

def optimizeFunc(num, x):
	return 0.5 * (x + num / x) # optimize function

print("{:.8f}".format(newtonMethod(9)))
print("{:.8f}".format(newtonMethod(2)))


# def sqrtNewton(target, x0, numIter):

# 	xNew = x0
# 	diff = target - xNew**2

# 	for i in range(0, numIter):
# 		xNew = iterToUpdate(target, xNew)
# 		diff = target - xNew**2
# 		if diff == 0:
# 			break
# 		print("{:.8f}->{:.8f}".format(xNew, target))

# 	return xNew


# def iterToUpdate(target, x):

# 	return x - (target - x**2) / (-2 * x)



# if __name__ == "__main__":

# 	target = 2.0
# 	x0 = 2.0
# 	res = sqrtNewton(target, x0, 500)

# 	print("Result: {:.10f}".format(res))
# 	print("Sqaure: {:.10f}".format(res**2))
