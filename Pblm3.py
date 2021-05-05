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
            self.distance = -1
            self.parent = None
            self.capacity = int(0xFFFFFF)

# A data structure for a vertex
class Edge:
	
	# Constructor to create a new vertex
	def __init__(self, vertex, weight):
            self.vertex = vertex 
            self.weight = weight


maxHeapSize = 0

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

def MaxHeapify(S, i):
    global maxHeapSize
    
    largest = None
    l = Left(i)
    r = Right(i)

    if l < maxHeapSize:
        if S[l].distance > S[i].distance:
            largest = l
        else:
            largest = i

    if r < maxHeapSize:
        if S[r].distance > S[largest].distance:
            largest = r

    if largest != None:
        if largest != i:
            swap(S, i, largest)
            MaxHeapify(S, largest)

def ExtractMax(A):
    global maxHeapSize
    if maxHeapSize < 1:
        return -1
    max = A[0]
    maxHeapSize -= 1
    A[0] = A[maxHeapSize]
    MaxHeapify(A,0)
    return max

def IncreaseKey(A, i, x):
    if x.distance < A[i].distance:
        return -1
    A[i].distance = x.distance
    while i > 0 and A[Parent(i-1)].distance < A[i].distance:
        swap(A, i, Parent(i-1))
        i = Parent(i-1)

def Insert(S, x):
    global maxHeapSize
    maxHeapSize += 1
    S.append(x)
    IncreaseKey(S, maxHeapSize-1, x)

def DijkstraCapacity(G, Start):
    # Graph, vertices, edges, and weights initialized during construction
    Start.distance = 0
    Start.capacity = 0

    # create vertex priority queue Q
    Q = []

    # initialize min-priority queue to contain all the vertices in G.V
    for i in range(0, len(G.V)):
        Insert(Q, G.V[i])

    u = ExtractMax(Q)                 # Remove and return best vertex
    while u is not -1:                  # The main loop
        
        for j in range(0,len(G.Adj[u.index])): # only v that are still in Q
            v = G.V[G.Adj[u.index][j].vertex]
            alt = u.distance + G.Adj[u.index][j].weight
            if (alt >= v.distance):
                v.distance = alt
                v.parent = u
                IncreaseKey(Q, v.index, v)
                if (v.capacity > G.Adj[u.index][j].weight):
                    v.capacity = G.Adj[u.index][j].weight

        u = ExtractMax(Q)                 # Remove and return best vertex

    return 


V = [Vertex(0),Vertex(1),Vertex(2),Vertex(3),Vertex(4),Vertex(5)]
E = [
    [Edge(1,1),Edge(2,7)],
    [Edge(3,9),Edge(5,15)],
    [Edge(4,4)],
    [Edge(5,5),Edge(4,10)],
    [Edge(5,3)],
    [],
   ]

G = Graph(V,E)

DijkstraCapacity(G, V[0])