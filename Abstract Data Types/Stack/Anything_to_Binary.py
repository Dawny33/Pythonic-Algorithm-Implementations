
def any_to_bin(number,base):
    digits = "0123456789ABCDEF"
	rem = Stack()

	while number > 0:
		reminder = number % base
		rem.push(reminder)
		number = number // base

	binary = ""
	while not rem.isEmpty():
		binary = binary + digits[rem.pop()]

	return binary


print(any_to_bin(42,8))