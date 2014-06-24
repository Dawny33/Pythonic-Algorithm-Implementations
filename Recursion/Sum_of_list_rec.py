def sum_rec(target):
	if len(target) == 1:
		return target[0]
	else:
		return target[0] + sum_rec(target[1:])	


#So, the code breaks the list recursively and compute the sum
#Ex: [3,5,7,9] is broken into (3 + (5 + (7 + 9))) and the ones in side the parantheses are solved
#stepwise.


#print sum_rec([1,3,5,7,9])		