import numpy as np
# use depth-first search to perform a topological sort of a directed acyclic graph (DAG)

#TOPOLOGICAL-SORT(G)
#   call DFS(G) to compute finishing times v.f for each vertex v
#   as each vertex is finished, insert it onto the front of a linked list
#   return the linked list of vertices

#DFS(G)
#   for each vertex u in V [G] do
#       color[u] = white
#       parent[u] = nil
#   time = 0
#   for each vertex u in V [G] do
#       if color[u] = white then DFS-VISIT[u]

#DFS-VISIT[u]
#   color[u] = grey (*u had been white/undiscovered*)
#   discover[u] = time
#   time = time + 1
#   for each v 2 Adj[u] do
#       if color[v] = white then
#           parent[v] = u
#           DFS-VISIT(v)
#   color[u] = black (*now nished with u*)
#   finish[u] = time
#   time = time + 1

color = []
parent = []
discover = []
finish = []
time = 0

def DFS_VISIT(u):
    global time
    color[G.index(u)] = 'grey'
    discover[G.index(u)] = time
    time = time + 1
# you are here    

def DFS(G):
    for v in G:
        color.append('white')
        parent.append(None)
    for u in G:
        if (color[G.index(u)] == 'white'):
            DFS_VISIT(u)




# create the adjacency matrix for our graph
G = [[1,3,6],[0,6],[5],[1,4],[1],[4,3],[3]]

DFS(G)