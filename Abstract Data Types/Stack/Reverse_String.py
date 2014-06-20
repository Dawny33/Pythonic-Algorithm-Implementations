class Stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.size() == 0

	def push(self,item):
		return self.items.insert(0,item)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

	def size(self):
		return len(self.items)	

#I tend to write the Stack implementation class in every example, just to \
# practise writing code. However it can simply be imported as a module too.

def Str_rev(target):

	stack_obj = Stack()
	for char in target:
	      stack_obj.push(char)

	 while not stack_obj.isEmpty():
            print(stack_obj.pop())

#An alternative implementation would be:
	for i in range(stack_obj.size()):
		print stack_obj.pop()
	

print(Str_rev("ABC"))