

#For creating a single node

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


#Now, we create the ordered list class

class OrderedList:

	def __init__(self):
		self.head = None

	def search(self, item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.getData() == item:
					found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()

		return found

#Traverses theough the list and adds in the item.
	def add(self, item):
		current = self.head
		previous = None
		stop = False
#The traversal going on. Previous is used, because we want to follow one position behind the current node
#in order to add. Ex: 31, 45, 56. We want to add 36. So, we traverse through the list and reach till 45.
#So, now we want to add the current number behind 45.				
		while current != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()
#If there is no previous, it means that the node is the head. Else, we need to insert the number and assign
#previous and next accordingly to the neighbouring elements.
		temp = Node(item)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current)
			previous.setNext(temp)	

	def isEmpty(self):
		return self.head == True

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count
			


#Examples for testing. Please uncomment, for usage.
# mylist = OrderedList()
# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)

# print(mylist.size())
# print(mylist.search(93))
# print(mylist.search(100))








