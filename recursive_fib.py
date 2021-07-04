def fib_recurs(x):
	if x == 0 or x == 1:
		return x
	return fib_recurs(x - 1) + fib_recurs(x - 2)


print(fib_recurs(7))
