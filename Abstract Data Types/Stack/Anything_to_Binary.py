

def any_to_bin(number,base):
	rem = Stack()

	while number > 0:
		reminder = number % base
		rem = rem.push(reminder)
		number //= base

	binary = ""
	while not rem.isEmpty():
		binary = binary + str(rem.pop())

	return binary
