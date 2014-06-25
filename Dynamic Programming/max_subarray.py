def max_subarray(a):

	s = -float('infinity')
	t = 0

	for i in range(len(a)):
		t = t + a[i]

		if t > s:
			s = t

		elif t < 0:
			t = 0

	return(s)


print max_subarray([1,2,-5,4,7,-2])
