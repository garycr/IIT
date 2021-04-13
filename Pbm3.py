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


G = [[1,3,6],[0,6],[5],[1,4],[1],[4,3],[3]]
#G = [[3],[2,7],[5,4],[5],[],[],[0,3,2],[4]]
# G = [[4,5,11],[2,4,8],[5,6,9],[2,6,13],[7],[8,12],[5],[],[7],[10,11],[13],[],[9],[]]

# A data structure for a vertex
class Vertex:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data 
		self.color = None
		self.distance = None
        self.parent = None

#  Given a graph G = (V, E) and a distinguished source vertex s
def BFS(G, s):
    for u in G: 
       u.color = 'WHITE'
       u.distance = int(0xFFFFFF)
       u.parent = None
    s.color = 'GRAY'
    s.distance = 0
    s.parent = None
    Q = 0
#   ENQUEUE(Q, s)
#   while Q != 0
#       u = DEQUEUE(Q)
#       for each v∈ G.Adj[u]
#          if v.color == 'WHITE'
#               v.color = 'GRAY'
#               v.distance = u.distance + 1
#               v.parent = u
#               ENQUEUE(Q, v)
#       u.color = 'BLACK'
    return

# example object intstanciation
root = Vertex(1)