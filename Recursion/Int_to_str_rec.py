def conv_rec(target, base):
	samplestr = "0123456789ABCDEF"

	if target < base:
		return samplestr[target]
	else:
		return conv_rec(target//base, base) + samplestr[target%base]


print(conv_rec(1453,16))
print type(conv_rec(675, 10))