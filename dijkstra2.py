#SELFMADE WELL MADE
# import the graph's "data structure"
from collections import defaultdict
import sys

class MinHeap():
    def __init__(self):
        self.array = []
        self.size = 0
        self.positions = []

    def swapNodes(self, key1, key2):
        #switch positions
        self.positions[self.array[key1][0]] = key2
        self.positions[self.array[key2][0]] = key1
        
        node = self.array[key1]
        self.array[key1] = self.array[key2]
        self.array[key2] = node

    def isMinHeap(self):
        return True if self.size > 0 else False
    
    def isInMinHeap(self, v):
        return True if self.positions[v] < self.size else False

    def decreaseKey(self, v, distance):
        #get the index of the node in minHeap array
        i = self.positions[v]

        #refresh the nodes value in minHeap
        self.array[i][1] = distance

        #correct the minHeap if needed
        while (i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]):
            self.swapNodes(i, (i - 1) // 2)

            #move on to the parent node (the one that we moved up)
            i = (i - 1) // 2

    def minHeapify(self, idx):
        smallest = idx
        left = idx * 2 + 1
        right = idx * 2 + 2

        if (left < self.size and self.array[left][1] < self.array[smallest][1]): 
            smallest = left
        if (right < self.size and self.array[right][1] < self.array[smallest][1]):
            smallest = right
        
        
        #if one of the children has a smaller path then swap it with his parent and start a recursion
        if smallest != idx:

            self.swapNodes(idx, smallest)
            self.minHeapify(smallest)

    def extractMin(self): 
        if self.isMinHeap() is not True:
            return

        minNode = self.array[0]

        #move the removed node out of the heap
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        self.positions[lastNode[0]] = 0
        self.positions[minNode[0]] = self.size - 1

        self.size = self.size - 1

        #correct the minHeap if needed
        self.minHeapify(0)

        return minNode


def printArr(distances, n):
	print ("Vertex\tDistance from source")
	for i in range(n):
		print ("%d\t\t%d" % (i,distances[i]))


class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    #function for adding nodes
    def addEdge(self, src, destination, weight):
        if (0 <= src < self.V and 0 < destination < self.V) == True:
            #edge from  (csource to dest and from dest to sourceuz undirected graph n shit)
            self.graph[src].insert(0, [destination, weight])
            self.graph[destination].insert(0, [src, weight])

    def dijkstra(self, src):
        
        #array for holding data of shortest paths, by index (at index 6 we would have the shortest path to edge 6)
        distances = []

        minHeap = MinHeap()
        minHeap.size = self.V

        for v in range (self.V):
            #currently marking the lengths of paths as "infinite values"
            distances.append(1e7)
            minHeap.array.append([v, distances[v]])
            minHeap.positions.append(v)

        #marking the path source node as 0
        distances[src] = 0
        minHeap.decreaseKey(src, 0)

        while minHeap.isMinHeap():
            #start finding new paths for the node with smallest path (currently)
            newHeapNode = minHeap.extractMin()
            heapKey = newHeapNode[0] 

            for keyCrawled in self.graph[heapKey]:
                v = keyCrawled[0]

                if (minHeap.isInMinHeap(v)
                    and distances[v] > distances[heapKey] + keyCrawled[1]
                    and distances[heapKey] != 1e7):
                    distances[v] = distances[heapKey] + keyCrawled[1]

                    minHeap.decreaseKey(v, distances[v])
            
        printArr(distances, self.V)

graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.dijkstra(0)
