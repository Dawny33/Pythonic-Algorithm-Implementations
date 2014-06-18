
def dec_to_bin(number):
	rem = Stack()

	while number > 0:
		reminder = number % 2
		rem.push(reminder)
		number = number  // 2

	binary = ""
	while not rem.isEmpty():
		binary = binary + str(rem.pop())

	return binary


#print(dec_to_bin(24))