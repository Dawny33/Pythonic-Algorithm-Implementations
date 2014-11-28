graph = { "a" : set(["b","s"]),
          "b" : set(["a"]),
          "s" : set(["c","g"]),
          "c" : set(["d","f","e"]),
          "g" : set(["f"]),
          "d" : set(["c"]),
          "f" : set(["c","g"]),
          "e" : set(["c","h"]),
          "h" : set(["g","e"])
    }



def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            #print visited
            queue.extend(graph[vertex] - visited)
            #print queue
    return visited


print bfs(graph, 'a')
