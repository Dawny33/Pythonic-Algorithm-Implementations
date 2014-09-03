
#The vertex data structure
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


#The overall Graph data structure

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


f = open("C:\\Users\\acer\\Desktop\\Pythonic-Algorithm-Implementations\\Abstract Data Types\\Graph\\Edges.txt")

g = Graph()
buff = []
buff1 = []
buff2 = []
#links = [[] for i in xrange(len(set(buff)))]
for line in f:
    buff1.append(line[0])
    buff2.append(line[2])
    buff.append(line[0])
    buff.append(line[2])

    g.addEdge(line[0],line[2])
    g.addEdge(line[2],line[0])

for v in g:
    print v

#for i in range(len(buff)):
#    g.addVertex(buff[i])

#for j in range(len(buff1)):
#    for k in range(len(buff2)):
#        g.addEdge(buff1[j],buff2[k])

print g.getVertices()
print g.getVertex(2)




f.close()

#print buff
#print set(buff)

