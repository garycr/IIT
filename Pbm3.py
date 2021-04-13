# use breadth-first search to perform a topological sort of a directed acyclic graph (DAG)

# There is another O(|V |+|E|) method for topological sort. Repeatedly find a vertex of
# in-degree 0, print it, and ”remove it from the graph” by adjusting the in-degree of the other nodes
# as if this node was removed.

# BFS(G, s)
#   for each vertex u ∈ G.V - {s}
#       u.color = WHITE
#       u.d = ∞
#       u.π = NIL
#   s.color = GRAY
#   s.d = 0
#   s.π = NIL
#   Q = Ø
#   ENQUEUE(Q, s)
#   while Q ≠ Ø
#       u = DEQUEUE(Q)
#       for each v∈ G.Adj[u]
#          if v.color == WHITE
#               v.color = GRAY
#               v.d = u.d + 1
#               v.π = u
#               ENQUEUE(Q, v)
#       u.color = BLACK


#G = [[1,3,6],[0,6],[5],[1,4],[1],[4,3],[3]]
#G = [[3],[2,7],[5,4],[5],[],[],[0,3,2],[4]]
# G = [[4,5,11],[2,4,8],[5,6,9],[2,6,13],[7],[8,12],[5],[],[7],[10,11],[13],[],[9],[]]

myQueue = []

# A data structure for a graph
class Graph:
	
	# Constructor to create a new node
	def __init__(self, v, e):
		self.V = v
		self.Adj = e

# A data structure for a vertex
class Vertex:
	
	# Constructor to create a new node
	def __init__(self, index):
            self.idx = index 
            self.color = 'WHITE'
            self.distance = int(0xFFFFFF)
            self.parent = None

#  Given a graph G = (V, E) and a distinguished source vertex s
def BFS(G, s):
    s.color = 'GRAY'
    s.distance = 0
    s.parent = None
    myQueue.append(s)
    
    while (len(myQueue) > 0):
        u = myQueue.pop(0)
        for i in G.Adj[u.idx]:
            v = G.V[i]
            if (v.color == 'WHITE'):
                v.color = 'GRAY'
                v.distance = u.distance + 1
                v.parent = u
                myQueue.append(v)
        u.color = 'BLACK'

    return u

def TP_SORT(G,s):

    w = BFS(G, s)

    result = []
    degree = 0
    while (degree <= w.distance): 
        for v in G.V:
            if (v.distance == degree):
                result.append(v.idx)
                G.V.remove(v)
        degree += 1

    return result



# example object instanciation

V = [Vertex(0),Vertex(1),Vertex(2),Vertex(3),Vertex(4),Vertex(5),Vertex(6) ]
E = [[1,3,6],[0,6],[5],[1,4],[1],[4,3],[3]]
G = Graph(V,E)

print(TP_SORT(G, V[0]))