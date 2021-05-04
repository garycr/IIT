# Problem 4 Counting Sort
import numpy as np

minVertex = 1
Q = []

# A data structure for a graph
class Graph:
	
	# Constructor to create a new graph
	def __init__(self, v, e):
		self.V = v
		self.Adj = e

# A data structure for a vertex
class Vertex:
	
	# Constructor to create a new vertex
	def __init__(self, index, distance):
            self.index = index 
            self.distance = distance
            self.parent = None

# A data structure for a vertex
class Edge:
	
	# Constructor to create a new vertex
	def __init__(self, vertex, weight):
            self.vertex = vertex 
            self.weight = weight

def COUNTING_SORT(A, k):
    C = np.zeros(k+1, dtype=int)
    #for i in range(0, len(C)):
    #    C[i] = 0
    for i in range(0, len(A)):
        C[A[i].distance] = C[A[i].distance] + 1
    
    # C[i] now contains the number of elements equal to i.
    for i in range(1,k+1):
        C[i] = C[i] + C[i - 1]
 
    # C[i] now contains the number of elements less than or equal to i.
    for j in range(len(A)-1, -1, -1):
       Q[C[A[j].distance]] = A[j]
       C[A[j].distance] = C[A[j].distance] - 1

    return

def ExtractMin(Q):
    global minVertex
    if minVertex > len(Q)-1:
        return -1
    min = Q[minVertex]
    minVertex = minVertex + 1
    return min

def DecreaseKey(Q, v, dv):
    COUNTING_SORT(v, dv)
    return


def Dijkstra(G, Start, MaxWeight):
    #Q = np.array(MaxWeight+1, dtype=Vertex)
    
    # initialize min-priority queue to contain all the vertices in G.V
    for i in range(0, len(G.V)+1):
        Q.append(Vertex(-1,-1))

    # initialize min-priority queue to contain all the vertices in G.V
    # create vertex priority queue Q
    COUNTING_SORT(G.V, MaxWeight)
    
    Start.distance = 0

    u = ExtractMin(Q)                 # Remove and return best vertex
    while u is not -1:                  # The main loop
        
        for j in range(0,len(G.Adj[u.index])): # only v that are still in Q
            v = G.V[G.Adj[u.index][j].vertex]
            alt = u.distance + G.Adj[u.index][j].weight
            if (alt <= v.distance):
                v.distance = alt
                v.parent = u
                DecreaseKey(Q, G.V, MaxWeight)

        u = ExtractMin(Q)                 # Remove and return best vertex

    return 

E = [
    [Edge(1,1),Edge(2,7)],
    [Edge(3,9),Edge(5,15)],
    [Edge(4,4)],
    [Edge(5,5),Edge(4,1)],
    [Edge(5,3)],
    [],
   ]

# determine the maximum weight possible
maxWeight = 0
for i in range(0,len(E)):
    for j in range(0,len(E[i])):
        maxWeight += E[i][j].weight

V = [Vertex(0,maxWeight),Vertex(1,maxWeight),Vertex(2,maxWeight),Vertex(3,maxWeight),Vertex(4,maxWeight),Vertex(5,maxWeight)]
G = Graph(V,E)
Dijkstra(G, V[0], maxWeight)