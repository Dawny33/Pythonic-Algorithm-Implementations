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




#Now, creating a Stack object

s = Stack()
s.push(4)
s.push("Dog")
s.push(True)

#print(s.size())
#print(s.peek())
#print(s.isEmpty())

s.push(8.4)	

#print(s.pop())
#print(s.pop())
#print(s.pop())
#print(s.pop())
