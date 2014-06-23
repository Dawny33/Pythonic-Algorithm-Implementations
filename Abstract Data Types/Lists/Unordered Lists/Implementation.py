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


#For creating a Linked List

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

#We always add the new item as the head of the list(most convenient).
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

#This method is famously called the Linked List traversal.
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

#Another linked-list traversal example.
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found


#Observe how the list is being sewn up, after removing a node.
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

# mylist = UnorderedList()

# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)

# print(mylist.size())
# print(mylist.search(93))
# print(mylist.search(100))

# mylist.add(100)
# print(mylist.search(100))
# print(mylist.size())

# mylist.remove(54)
# print(mylist.size())
# mylist.remove(93)
# print(mylist.size())
# mylist.remove(31)
# print(mylist.size())
# print(mylist.search(93))
