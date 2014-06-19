
def Hot_Pop(names, num):
	stack_imp = Queue()

	for i in names:
		stack_imp.enqueue(i)

	while stack_imp.size() > 1:
		for j in range(num):
			stack_imp.enqueue(stack_imp.dequeue())

		stack_imp.dequeue()

	return stack_imp.dequeue()		


#print(Hot_Pop(["Bill","David","Susan","Jane","Kent","Brad"],7))

