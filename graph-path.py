# Python program to generate the first 
# path of the graph from the nodes provided 
  
graph = { 
    'a': ['c'], 
    'b': ['d'], 
    'c': ['e'], 
    'd': ['a', 'd'], 
    'e': ['b', 'c', 'f'],
    'f': ['a']
} 
  
# function to find path 
  
  
def find_path(graph, start, end, path=[]): 
    path = path + [start] 
    if start == end: 
        return path 
    for node in graph[start]: 
        if node not in path: 
            newpath = find_path(graph, node, end, path) 
            if newpath: 
                return newpath 
  
  
# Driver function call to print the path 
print(find_path(graph, 'a', 'f')) 