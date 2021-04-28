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
        x1 = 0
        y1 = 0
        x2 = L[1]
        y2 = max(points[:,0])
        R.append([x1,y1,x2,y2])
    
        x1 = 0
        y1 = L[1]
        x2 = max(points[:,1])
        y2 = max(points[:,0])
        R.append([x1,y1,x2,y2])
    else:
        x1 = 0
        y1 = 0
        x2 = L[1]
        y2 = max(points[:,0])
        R.append([x1,y1,x2,y2])
    
        x1 = L[1]
        y1 = 0
        x2 = max(points[:,1])
        y2 = max(points[:,0])
        R.append([x1,y1,x2,y2])

    return


def CoveredPoints(boundingRectangle, points):
    pts = 0

    for i in range(0, len(points)):
        x = points[i][0]
        y = points[i][1]
        x1 = boundingRectangle[0]
        y1 = boundingRectangle[1]
        x2 = boundingRectangle[2]
        y2 = boundingRectangle[3]

        if ((x >= x1 and x <= x2) and (y >= y1 and y <= y2)):
            pts += 1

    return pts

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
x1 = np.concatenate([r[2,:3], r[0,2:3]])
x2 = np.concatenate([r[1,:2], r[2,2:4]])
x3 = np.concatenate([r[3,0:1], r[1,1:2], r[3,2:]])
x4 = np.concatenate([r[3,0:3], r[1,1:2]])

pts1 = CoveredPoints(x1, points)
pts2 = CoveredPoints(x2, points)
pts3 = CoveredPoints(x3, points)
pts4 = CoveredPoints(x4, points)

########################################################
# see if we should do a horizontal or vertical line next
if (pts2 + pts3 > pts1 + pts4):
    #horizontal
    ux = mean(points[:,0]) - 0.5
    L = ['h', ux]
    S.append(L)
    BoundedRects(L)
else:
    #vertical
    uy =  mean(points[:,0]) + 0.5
    L = ['v', uy]
    S.append(L)
    BoundedRects(L)


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
print("Done")