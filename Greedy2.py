import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

# load the instance file
fileNm = 'instance01.csv'
points = np.loadtxt(fileNm, skiprows=1, dtype=int)

S = []
R = []

def BoundedRects(L):
    if (L[0] == 'h'):
        x = 0
        y = 0
        h = L[1]
        w = max(points[:,0])
        R.append([x,y,h,w])
    
        x = 0
        y = L[1]
        h = max(points[:,1])
        w = max(points[:,0])
        R.append([x,y,h,w])
    else:
        x = 0
        y = 0
        h = max(points[:,0])
        w = L[1]
        R.append([x,y,h,w])
    
        x = L[1]
        y = 0
        h = max(points[:,1])
        w = max(points[:,0])
        R.append([x,y,h,w])

    return

# start with initial partition
ux = mean(points[:,0]) - 0.5
uy =  mean(points[:,0]) + 0.5

tx = sum(points[:,0] > ux)
ty = sum(points[:,1] > uy)

# horizontal line
L = ['h', ux]
S.append(L)
BoundedRects(L)

# vertical line
L = ['v', uy]
S.append(L)
BoundedRects(L)

r = np.array(R)
txMax = max(r[:,0])
txMin = min(r[:,0])

tyMax = max(r[:,1])
tyMin = min(r[:,1])

# Verify rectangles
x1 = np.concatenate([r[0,:3], r[2,3:4]])
x2 = np.concatenate([r[0,:2], r[2,2:4]])
x3 = np.concatenate([r[3,0:1], r[1,1:2], r[3,2:]])
x4 = np.concatenate([r[3,0:1], r[1,1:2], r[0,2:4]])

result = sum(points[:,0] > x1[3] and points[:,1] < x1[2])


for i in range(0, len(S)):
    if (S[i][0] == 'h'):
        plt.axhline(y=S[i][1], color='r', linestyle='-')
    else:
        plt.axvline(x=S[i][1], color='b', linestyle='-')


# plot the points
plt.scatter(points[:,0], points[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.show()