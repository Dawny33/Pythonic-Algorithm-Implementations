class Queue:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self,item):
		return self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)		
		


# q = Queue()
# #print(q.isEmpty())
# q.enqueue(2)
# print(q.isEmpty())

# q.dequeue()
# print(q.isEmpty())