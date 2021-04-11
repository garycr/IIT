import numpy as np

E = ([[0,1,0],[0,0,1],[1,1,0]])
E2 = ([[0,1,0],[0,0,1],[1,1,0]])

n = len(E)
k = len(E2[0])
m = len(E2)

# Given the existence of A an m x n matrix and B an n x p matrix
# The following algorithm is used to multiply A x B

# To begin, we need to initialize the resultant matrix to zeros
C = np.zeros((n,k), dtype=int)

# The algorithm to do the matrix multiplication follows
for i in range(0,len(E)) :
    for j in range(0,len(E2[0])) :
        C[i][j] = 0
        for k in range(0,len(E2)) :
            if (E[i][j] == 1 and E[j][i] == 1):
                C[i][j] += E[i][k] * E[k][j]

print(C)


