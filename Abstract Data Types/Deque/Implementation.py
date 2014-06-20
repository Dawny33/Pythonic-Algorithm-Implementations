class Deque:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		return self.items.append(item)
	
	def addRear(self,item):
		return self.items.insert(0,item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return	self.items.pop(0)

	def size(self):
		return len(self.items)


		
# p = Deque()
# p.addFront(2)
# p.addRear(True)

# print(p.removeFront())
# print(p.removeFront())
