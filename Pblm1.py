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
            self.color = 'White'

# A data structure for a vertex
class Edge:
	
	# Constructor to create a new vertex
	def __init__(self, vertex, weight):
            self.vertex = vertex 
            self.weight = weight

# G=Graph, W=Weight, sV =Source Vertex
def MODIFIED_PRIM(G,sV):
    # Graph, vertices, edges, and weights initialized during construction

    min = int(0xFFFFFF)
    idx = -1
    for i in range(0, len(G.Adj[sV.index])): 
        e = G.Adj[sV.index][i]
        if (e.vertex.color = 'White' and e.weight < min ):
            min = e.weight
            idx = i

    sV.color = 'Black'
    sV.distance = min
    sV = G.Adj[idx].vertex 






        v = G.V[G.Adj[u.index][j].vertex]
        alt = u.distance + G.Adj[u.index][j].weight
        if (alt <= v.distance):
            v.distance = alt
            v.parent.append(u)
            DecreaseKey(Q, v.index, v)


    return 


V = [Vertex(0),Vertex(1),Vertex(2),Vertex(3),Vertex(4),Vertex(5)]
E = [
    [Edge(1,1),Edge(2,7)],
    [Edge(3,9),Edge(5,15)],
    [Edge(4,4)],
    [Edge(5,5),Edge(4,1)],
    [Edge(5,3)],
    [],
   ]

G = Graph(V,E)

MODIFIED_PRIM(G, V[0])