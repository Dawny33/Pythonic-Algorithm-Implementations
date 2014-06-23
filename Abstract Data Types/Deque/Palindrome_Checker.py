

def checker(palin):
	outdeq = Deque()

	for i in palin:
		outdeq.addRear(i)

	Equal = True

	while (outdeq.size() > 1) and  Equal:	
		first = outdeq.removeFront()
		last = outdeq.removeRear()

		if first.lower() != last.lower():
			Equal = False
		else:
			Equal

	return Equal


#print checker("Noon")
