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

# create the adjacency matrix for our graph
G = [[1,3,6],[0,6],[5],[1,4],[1],[4,3],[3]]
#G = [[3],[2,7],[5,4],[5],[],[],[0,3,2],[4]]
#G = [[4,5,11],[2,4,8],[5,6,9],[2,6,13],[7],[8,12],[5],[],[7],[10,11],[13],[],[9],[]]
#G = [['q','r','x'],['o','q','u'],['r','s','v'],['o','s','z'],['t'],['u','y'],['r'],[],['t'],['w','x'],['z'],[],['v'],[]]


color = []
parent = []
discover = []
finish = []
tpSort = []
# labels = ['m', 'n','o','p','q','r','s','t','u','v','w','x','y','z']
labels = ['0', '1','2','3','4','5','6']
time = 0

def DFS_VISIT(u):
    global time
    color[u] = 'grey'
    discover[u] = time
    time = time + 1

    for v in G[u]:
        if (color[v] == 'white'):
            parent[v] = u
            DFS_VISIT(v)
    
    color[u] = 'black'
    finish[u] = time
    tpSort.append(labels[u])
    time = time + 1


def DFS(G):
    for v in range(0, len(G)):
        color.append('white')
        parent.append(None)
        discover.append(None)
        finish.append(None)
    for u in range(0, len(G)):
        if (color[u] == 'white'):
            DFS_VISIT(u)


DFS(G)

print(discover)
print(finish)
tpSort.reverse()
print(tpSort)