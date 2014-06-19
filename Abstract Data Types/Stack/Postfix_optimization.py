
def postfix_opt(target):
	operandstack = Stack()
	tokenList = target.split()

	for token in tokenList:
		if token in "1234567890" :
			operandstack.push(int(token))
		else:
			second = operandstack.pop()	
			first = operandstack.pop()
			result = doMath(token,first,second)
			operandstack.push(result)
	return operandstack.pop()

def doMath(op, op1, op2):
	if op == "+":
		return op1 + op2
	elif op == "*":
		return op1 * op2
	elif op == "/":
		return op1 / op2
	elif op  == "-":
		return op1 - op2
	else:
		return op1 ^ op2	



print(postfix_opt('7 8 + 3 2 + /'))
