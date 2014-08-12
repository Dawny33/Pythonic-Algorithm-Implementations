#Hash Table implementation.

class HashTable:
    
#The constructor module.
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

#The put(insert) module.
    def put(self,key,data):
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
                    
#The get(retrieve) module.
    def get(self,key):
          startslot = self.hashfunction(key,len(self.slots))

          data = None
          stop = False
          found = False
          position = startslot
          while self.slots[position] != None and  not found and not stop:
             if self.slots[position] == key:
                found = True
                data = self.data[position]
             else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
          return data

#The get item constructor module.
    def __getitem__(self,key):
        return self.get(key)

#The set item constructor module
    def __setitem__(self,key,data):
        self.put(key,data)


H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"

print H.slots
print H.data
