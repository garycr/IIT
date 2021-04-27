import numpy as np
import matplotlib.pyplot as plt

# load the instance file
fileNm = 'instance01.csv'
points = np.loadtxt(fileNm, skiprows=1, dtype=int)


while True:
    mx = max(points[:,0])
    mn = min(points[:,0])
    x = (mx - mn)
    hline = x if x % 2 else x + 1
    hline =  (x / 2)

    mx = max(points[:,1])
    mn = min(points[:,1])
    y = (mx - mn)
    vline = y if y % 2 else y + 1
    vline =  (y / 2) + mn

    plt.axhline(y=hline, color='r', linestyle='-')
    plt.axvline(x=vline, color='b', linestyle='-')


    above = sum(points[:,0] > hline)
    below = sum(points[:,0] < hline)

    right = sum(points[:,1] > vline)
    left = sum(points[:,1] < vline)

    p = (points[points[:,0] > hline])
    mx = max(p[:,0])
    mn = min(p[:,0])
    x = (mx - mn)
    hline = x if x % 2 else x + 1
    hline =  (x / 2) + mn
    plt.axhline(y=hline, color='r', linestyle='-')

    break

# plot the points
plt.scatter(points[:,0], points[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.show()