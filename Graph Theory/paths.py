graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

def find_path(graph,start,end,path = []):
    path += start
    if start == end:
        return path

    if start not in graph:
        return None

    else:
        for vertex in graph[start]:
            if vertex not in path:
                ext_path = find_path(graph,vertex,end,path)

                if ext_path:
                    return ext_path

print find_path(graph,"a","e")

def find_all_paths(graph,start,end,path = []):
    path += start
    if start == end:
        return path

    if start not in graph:
        return []

    else:
        all_paths = []
        for vertex in graph[start]:
            if vertex not in path:
                ext_path = find_all_paths(graph,vertex,end,path)

                for p in ext_path:
                    all_paths.append(p)
        return all_paths
                    
print find_all_paths(graph,"d","e")

