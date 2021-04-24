import numpy as np
#from bitarray import bitarray

# A data structure for a graph
class Graph:
	
	# Constructor to create a new node
	def __init__(self, v, e):
		self.V = v
		self.Adj = []

# A data structure for a vertex
class Vertex:
	
	# Constructor to create a new node
	def __init__(self, index, degree, adj):
		self.index = index 
		self.degree = degree
		self.adj = adj

'''
16.1 Clique
A maximal clique is a clique that cannot be enlarged by adding any additional vertex. This doesn't mean that it 
has to be large relative to the largest possible clique, but it might be. To find a nice maximal (and hopefully large)
clique, sort the vertices from highest degree to lowest degree, put the first vertex in the clique, and then test each 
of the other vertices to see whether it is adjacent to all the clique vertices added thus far. If so, add it; if not, 
continue down the list. By using a bit vector to mark which vertices are currently in the clique, this can be made to 
run in O (n + m) time. An alternative approach might incorporate some randomness into the vertex ordering, and accept 
the largest maximal clique you find after certain number of trials.
'''



# Put the first vertex in the clique, and then test each of the other vertices to see whether it is adjacent to 
# all the clique vertices added thus far

# If so, add it; if not, continue down the list.

# Use a bit vector to mark which vertices are currently in the clique

def sortKey(obj):
	return obj.degree

def MaximalClique(E):

	G = []
	C = 0

	# Add each vertex to a graph and determine its degree
	for n in range(0, len(E)):
		bv = 0
		for e in range(0,len(E[n])):
			bv += 1 << E[n][e]
		G.append(Vertex(n, len(E[n]), bv))

	# Sort the vertices from highest degree to lowest degree
	G.sort(key=sortKey, reverse=True)

	# Put the first vertex in the clique
	C = 1 << G[0].index


	for v in range(1,len(G)):
		# Test each of the other vertices to see whether it is adjacent to all the clique vertices added thus far
		test = True

		# Use a bit vector to mark which vertices are currently in the clique
		if ((C & G[v].adj) == C):
			C += 1 << G[v].index

	return C


#E = [[1,4],[0,2,3,4],[1,3],[1,4,2],[3,0,1]]
E = [[1,4,3],[0,2,3,4],[1,3],[0,1,4,2],[3,0,1]]
# G = [[4,5,11],[2,4,8],[5,6,9],[2,6,13],[7],[8,12],[5],[],[7],[10,11],[13],[],[9],[]]




result = MaximalClique(E)
print(result)