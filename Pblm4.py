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

# A data structure for a vertex
class Edge:
	
	# Constructor to create a new vertex
	def __init__(self, vertex, weight):
            self.vertex = vertex 
            self.weight = weight


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

def DecreaseKey(A, i, x):
    if x.distance > A[i].distance:
        return -1
    A[i].distance = x.distance
    while i > 0 and A[Parent(i-1)].distance > A[i].distance:
        swap(A, i, Parent(i-1))
        i = Parent(i-1)

def Insert(S, x):
    global minHeapSize
    minHeapSize += 1
    S.append(x)
    DecreaseKey(S, minHeapSize-1, x)

# G=Graph, W=Weight, S=Source Vertex
def Dijkstra(G,S):
    # Graph, vertices, edges, and weights initialized during construction
    S.distance = 0

    # create vertex priority queue Q
    Q = []

    # initialize min-priority queue to contain all the vertices in G.V
    for i in range(0, len(G.V)):
        Insert(Q, G.V[i])

    u = ExtractMin(Q)                 # Remove and return best vertex
    while u is not -1:                  # The main loop
        
        for j in range(0,len(G.Adj[u.index])): # only v that are still in Q
            v = G.V[G.Adj[u.index][j].vertex]
            alt = u.distance + G.Adj[u.index][j].weight
            if (alt < v.distance):
                v.distance = alt
                v.parent = u
                DecreaseKey(Q, v.index, v)

        u = ExtractMin(Q)                 # Remove and return best vertex

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

Dijkstra(G, V[0])