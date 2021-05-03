import numpy as np

# A data structure for a vertex
class Edge:
	
	# Constructor to create a new vertex
	def __init__(self, u, v, weight):
            self.u = u 
            self.v = v
            self.weight = weight
            self.color = 'White'

def min(M,V):
    
    min = int(0xFFFFFF)
    idx = -1

    for i in range(0,len(V)):
        for j in range(0, len(V)):
            if (V[i] == 'Black' and M[i][j] > 0 and M[i][j] < min and V[j] != 'Black'):
                idx = j
                min = M[i][j]
    return (idx, min)

def MODIFIED_PRIM(M,V,start):
    distance = 0
    
    V[start] = 'Black'
    idx, weight = min(M,V)
 
    while (idx != -1):
        V[idx] = 'Black'
        distance = distance + weight
        idx, weight = min(M,V)
    return 


def LoadMatrix(M, E):
    for i in range(0,len(E)):
        M[E[i].u, E[i].v] = E[i].weight


V = ['White','White','White','White','White','White','White','White','White']

E1 = [Edge(0,1,4),
     Edge(1,0,4),
     Edge(1,2,8),
     Edge(2,1,8),
     Edge(0,7,13),
     Edge(7,0,13),
     Edge(2,3,12),
     Edge(3,2,12),
     Edge(3,4,9),
     Edge(4,3,9),
     Edge(4,5,10),
     Edge(5,4,10),
     Edge(5,6,3),
     Edge(6,5,3),
     Edge(6,7,1),
     Edge(7,6,1),
     Edge(2,8,2),
     Edge(8,2,2),
     Edge(2,5,5),
     Edge(5,2,5),
     Edge(3,5,14),
     Edge(5,3,14),
     Edge(6,8,6),
     Edge(8,6,6),
     Edge(7,8,7),
     Edge(8,7,7)
    ]

M = np.zeros((len(E1),len(E1)), dtype=int)
LoadMatrix(M,E1)
MODIFIED_PRIM(M,V,0)