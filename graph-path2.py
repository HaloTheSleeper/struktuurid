graph = { 
    'a': ['c'], 
    'b': ['d'], 
    'c': ['e'], 
    'd': ['a', 'd'], 
    'e': ['b', 'c', 'f'],
    'f': ['a']
} 

def findPath(graph, start, end, path=[]):
    path = path + [start]
    
    if start == end:
        return path
    
    for node in graph[start]:
        if node not in path:
            newPath = findPath(graph, node, end, path)
            if newPath:
                return newPath
            

print(findPath(graph, 'a', 'f'))