graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

def generate_edges(graph):
    edges = []

    for node in graph:
        for neighbour in graph[node]:
            edges.append((node,neighbour))
            
    return edges

print generate_edges(graph)

def isolated_nodes(graph):
    isolated = []
    for node in graph:
        if graph[node] == []:
            isolated += node
    return isolated

print isolated_nodes(graph)
