graph = {"a" : ["d"],
         "b" : ["c"],
         "c" : ["c","d","b","e"],
         "d" : ["a","c"],
         "e" : ["c"],
         "f" : []
    }

def degree(graph,vertex):
    deg = len(graph[vertex]) + graph[vertex].count(vertex)
    return deg

print degree(graph,"f")
