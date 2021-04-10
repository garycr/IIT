import numpy as np

A = ([[0,1,0],[0,0,1],[1,1,0]])
B = ([[0,1,0],[0,0,1],[1,1,0]])

n = len(A)
k = len(B[0])
m = len(B)

# Given the existence of A an m x n matrix and B an n x p matrix
# The following algorithm is used to multiply A x B

# To begin, we need to initialize the resultant matrix to zeros
C = np.zeros((n,k), dtype=int)

# The algorithm to do the matrix multiplication follows
for i in range(0,len(A)) :
    for j in range(0,len(B[0])) :
        C[i][j] = 0
        for k in range(0,len(B)) :
            if (A[i][j] == 1 and B[j][i] == 1):
                C[i][j] += A[i][k] * B[k][j]

print(C)


