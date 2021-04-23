import numpy as np

# A data structure for a graph
class Graph:
	
	# Constructor to create a new graph
	def __init__(self, v, e):
		self.V = v
		self.Adj = e

# A data structure for a vertex
class Vertex:
	
	# Constructor to create a new vertex
	def __init__(self, index):
            self.index = index 
            self.distance = int(0xFFFFFF)
            self.parent = None

minHeapSize = 0

def Parent(i):
    return int(i/2)

def Left(i):
    return (2 * (i + 1)) - 1

def Right(i):
    return Left(i) + 1

def swap(ls, a, b):
    tmp = ls[a]
    ls[a] = ls[b]
    ls[b] = tmp
    return

def MinHeapify(S, i):
    global minHeapSize
    
    smallest = i
    l = Left(i)
    r = Right(i)

    if l < minHeapSize:
        if S[l].distance < S[i].distance:
            smallest = l
        else:
            smallest = i

    if r < minHeapSize:
        if S[r].distance < S[smallest].distance:
            smallest = r

    if smallest != None:
        if smallest != i:
            swap(S, i, smallest)
            MinHeapify(S, smallest)

def ExtractMin(A):
    global minHeapSize
    if minHeapSize < 1:
        return -1
    min = A[0]
    A[0] = A[minHeapSize-1]
    minHeapSize -= 1
    MinHeapify(A,0)
    return min

def minHeapIncreasedistance(A, i, x):
    if x.distance > A[i].distance:
        return -1
    A[i] = x
    while i > 0 and A[Parent(i-1)].distance > A[i].distance:
        swap(A, i, Parent(i-1))
        i = Parent(i-1)

def Insert(S, x):
    global minHeapSize
    minHeapSize += 1
    S[minHeapSize-1] = x
    minHeapIncreasedistance(S, minHeapSize-1, x)


# G=Graph, W=Weight, S=Source Vertex
def Dijkstra(G, W, S):
    # Graph, vertices, edges, and weights initialized during construction
3
4      create vertex priority queue Q
5
6      for each vertex v in Graph:          
7          if v ≠ source
8              dist[v] ← INFINITY                 // Unknown distance from source to v
9              prev[v] ← UNDEFINED                // Predecessor of v
10
11         Q.add_with_priority(v, dist[v])
12
13
14     while Q is not empty:                      // The main loop
15         u ← Q.extract_min()                    // Remove and return best vertex
16         for each neighbor v of u:              // only v that are still in Q
17             alt ← dist[u] + length(u, v)
18             if alt < dist[v]
19                 dist[v] ← alt
20                 prev[v] ← u
21                 Q.decrease_priority(v, alt)
22
23     return dist, prev

V = [Vertex(0),Vertex(1),Vertex(2),Vertex(3),Vertex(4),Vertex(5),Vertex(6)]
E = [[1,3,6],[0,6],[5],[1,4],[1],[4,3],[3]]
G = Graph(V,E)