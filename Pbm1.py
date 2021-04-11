import numpy as np

E = ([[0,1,0],[1,0,1],[1,1,0]])
n = len(E)
k = len(E[0])

E2 = np.zeros((n,k), dtype=int)

for i in range(0,len(E)) :
    for j in range(i+1,len(E[0])) :
        E2[i][j] = 0
        if (E[i][j] == 1 and E[j][i] == 1):
            E2[i][j] = E[i][j] 
            E2[j][i] = E[j][i]

print(E2)


