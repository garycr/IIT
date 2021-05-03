# Mistakenly did the problem with Adjaceny list instead of matrix


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
	def __init__(self, u, v, weight):
            self.u = u 
            self.v = v
            self.weight = weight
            self.color = 'White'

def min(V, E, idx):
    
    min = int(0xFFFFFF)
    e = -1

    for i in range(0,len(E)):
        #if (V[E[i].u].color == 'Black' and E[i].color == 'White' and E[i].weight < min and V[E[i].v].color != 'Black'):
        if (E[i].color == 'Grey' and E[i].color == 'White' and E[i].weight < min and V[E[i].v].color != 'Black'):
            e = E[i]
            min = e.weight
    if (e != -1):
        e.color = 'Grey'
    return e


# G=Graph, W=Weight, sV =Source Vertex
def MODIFIED_PRIM(G,sV):
    # Graph, vertices, edges, and weights initialized during construction
    idx = sV.index
    G.V[idx].color = 'Black'
    e = min(G.V, G.Adj, idx)
 
    while (e != -1):
        G.V[e.v].color = 'Black'
        G.V[e.v].distance = G.V[e.v].distance + e.weight
        e = min(G.V, G.Adj, e.v)
    return 

V = [Vertex(0),Vertex(1),Vertex(2),Vertex(3),Vertex(4),Vertex(5),Vertex(6),Vertex(7),Vertex(8)]

E = [Edge(0,1,4),
     Edge(1,0,4),
     Edge(1,2,8),
     Edge(2,1,8),
     Edge(0,7,8),
     Edge(7,0,8),
     Edge(2,3,7),
     Edge(3,2,7),
     Edge(3,4,9),
     Edge(4,3,9),
     Edge(4,5,10),
     Edge(5,4,10),
     Edge(5,6,2),
     Edge(6,5,2),
     Edge(6,7,1),
     Edge(7,6,1),
     Edge(2,8,2),
     Edge(8,2,2),
     Edge(2,5,4),
     Edge(5,2,4),
     Edge(3,5,14),
     Edge(5,3,14),
     Edge(6,8,6),
     Edge(8,6,6),
     Edge(7,8,7),
     Edge(8,7,7)
    ]

G = Graph(V,E)
MODIFIED_PRIM(G, V[0])