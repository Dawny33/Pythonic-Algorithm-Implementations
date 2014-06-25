def fibo_dp(n):
	n2, n1 = 0, 1

	for i in range(0, n-2):
		n2, n1 = n1, n1+n2

	return n2  + n1

print fibo_dp(5)	
