#Hash Table implementation.

class HashTable:
    
#The constructor module.
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.size = [None] * self.size

#The put(insert) module.
    def put(self,key,value):
        hashvalue = self.hashfun(key, len(self.slots))

        if self.slots == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while (self.slots[nextslot] != None) and (self.slots[nextslot] != key):
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

#The hashfunc module
    def hashfun(self,key,size):
        return key%size

#The re-hashfunc module for handling collisions.
    def rehash(slf, oldhash, size):
        return (oldhash+1)%size
                    
