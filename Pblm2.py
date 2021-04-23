import numpy as numpy

# A data structure for a graph
class Graph:
	
	# Constructor to create a new node
	def __init__(self, v, e):
		self.V = v
		self.Adj = []

# A data structure for a vertex
class Vertex:
	
	# Constructor to create a new node
	def __init__(self, index, degree):
            self.idx = index 
            self.degree = degree

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
	C = [] 		# Clique

	# Add each vertex to a graph and determine its degree
	for n in range(0, len(E)):
		G.append(Vertex(n, len(E[n])))

	# Sort the vertices from highest degree to lowest degree
	G.sort(key=sortKey, reverse=True)

	# Put the first vertex in the clique
	C.append(G[0])

	for m in range(1,len(G)):
		# Test each of the other vertices to see whether it is adjacent to all the clique vertices added thus far
		

		# If so, add it; if not, continue down the list.

		# Use a bit vector to mark which vertices are currently in the clique

	return G


E = [[2,5],[1,5,3,4],[2,4],[2,5,3],[4,1,2]]
#G = [[3],[2,7],[5,4],[5],[],[],[0,3,2],[4]]
# G = [[4,5,11],[2,4,8],[5,6,9],[2,6,13],[7],[8,12],[5],[],[7],[10,11],[13],[],[9],[]]

MaximalClique(E)