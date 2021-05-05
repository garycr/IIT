import numpy as np

# A data structure for a graph
class Graph:
	
	# Constructor to create a new node
	def __init__(self, v, e):
		self.V = v
		self.Adj = e

# A data structure for a vertex
class Vertex:
	
	# Constructor to create a new node
	def __init__(self, index, label):
            self.idx = index
            self.lbl = label 
            self.color = 'white'
            self.distance = int(0xFFFFFF)
            self.parent = None
            self.capacity = 0
            self.discover = None

# A data structure for a vertex
class Edge:
	
	# Constructor to create a new vertex
	def __init__(self, vertex, weight):
            self.vertex = vertex 
            self.weight = weight
            self.color = 'white'

path = []

def DFS_VISIT(G, u):
    for e in G.Adj[u.idx]:
        v = G.V[e.vertex]
        if (v.color == 'white'):
            v.parent = u
            v.capacity = e.weight
            DFS_VISIT(G,v)
    path.append([u.lbl, u.capacity])
    return 

V = [Vertex(0,'S'),Vertex(1,'U'),Vertex(2,'V')]

E = [
    [Edge(1,7)],
    [Edge(2,3)],
    []
   ]


#V = [Vertex(0,'S'),Vertex(1,'U'),Vertex(2,'V'),Vertex(3,'T')]
#E = [
#    [Edge(1,7),Edge(2,5),Edge(3,6)],
#    [Edge(3,3),Edge(2,10)],
#    [Edge(1,5),Edge(3,9)],
#    []
#   ]

G = Graph(V,E)
DFS_VISIT(G, V[0])
print(path)