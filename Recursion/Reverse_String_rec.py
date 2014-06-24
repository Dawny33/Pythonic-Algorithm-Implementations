def rev_str(target):
	if len(target) == 1:
		return target
	else:
		return rev_str(target[1:]) + target[0]


# print rev_str("Pikachu")