import numpy as np
import matplotlib.pyplot as plt

S = []
R = []
numPoints = 0

# A data structure for a rectangle
class Rectangle:
	
	# Constructor to create a new recetangle
	def __init__(self, x1, y1, x2, y2):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
            self.points = []

# A data structure for a point
class Point:
	
	# Constructor to create a new point
	def __init__(self, index, x, y):
            self.idx = index 
            self.x = x
            self.y = y

def Plot():
    global numPoints
    # plot the output
    for i in range(0, len(S)):
        if (S[i][0] == 'h'):
            plt.axhline(y=S[i][1], color='r', linestyle='-')
        else:
            plt.axvline(x=S[i][1], color='b', linestyle='-')
    
    points = np.zeros((numPoints,2), dtype=int)
    idx = 0
    for j in range(0,len(R)):
        for i in range(0,len(R[j].points)):
            points[idx][0] = R[j].points[i].x
            points[idx][1] = R[j].points[i].y
            idx += 1
    
    # plot the points
    plt.scatter(points[:,0], points[:,1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def MovePoints(OriginalRect, NewRect, LineType):
    ToBeMoved = []

    for i in range(0, len(OriginalRect.points)):
        pt = OriginalRect.points[i]
        
        if ((LineType == 'h' and (pt.y < OriginalRect.y1 or pt.y > OriginalRect.y2)) or
           (LineType == 'v' and (pt.x < OriginalRect.x1 or pt.x > OriginalRect.x2))):
            ToBeMoved.append(pt)

    for j in range(0,len(ToBeMoved)):
        OriginalRect.points.remove(ToBeMoved[j])
        NewRect.points.append(ToBeMoved[j])

    return

def SplitRect(NewLine, OldRect):
    if (NewLine[0] == 'h'):
        # create a new rectangle for the split
        newRect = Rectangle(x1=OldRect.x1, y1=NewLine[1], x2= OldRect.x2, y2= OldRect.y2)
        R.append(newRect)                
        # update the existing rectangle y2 coordinate
        OldRect.y2 = NewLine[1]
        MovePoints(OldRect, newRect, NewLine[0])
    elif (NewLine[0] == 'v'):
        # create a new rectangle for the split
        newRect = Rectangle(x1=NewLine[1], y1=OldRect.y1, x2= OldRect.x2, y2= OldRect.y2)
        R.append(newRect)                
        # update the existing rectangle x2 coordinate
        OldRect.x2 = NewLine[1]
        MovePoints(OldRect, newRect, NewLine[0])
    return

# determine the number of rectangles 
def BoundedRects(L):
    for i in range(0, len(R)):
        if (L[0] == 'v' and L[1] > R[i].x1 and L[1] < R[i].x2):
            SplitRect(L, R[i])
        elif (L[0] == 'h' and L[1] > R[i].y1 and L[1] < R[i].y2):
            SplitRect(L, R[i])


def Partition(Rect):
    # use the mean of the points
    ux = 0
    uy = 0
    pts = len(Rect.points)
    for i in range(0, pts):
        ux += Rect.points[i].x
        uy += Rect.points[i].y
    
    meanX = 0
    meanY = 0
    if (pts > 0):
        meanX = ux/pts
        meanY = uy/pts

    if ((meanX % 1) == 0):
        meanX += 0.5
    
    if ((meanY % 1) == 0):
        meanY += 0.5

    xPoints = 0
    yPoints = 0
    for j in range(0, pts):
        if (Rect.points[j].x > meanX):
            xPoints += 1
        if (Rect.points[j].y > meanY):
            yPoints += 1

    return (meanX, xPoints, meanY, yPoints)

def Done():
    
    done = True
    for i in range(0, len(R)):
        if (len(R[i].points) > 1):
            done = False
            break

    return done

def CreateLines():
    
    while (Done() != True):
    
        maxPts = []

        for i in range(0,len(R)):
            #xMean, xPts, yMean, yPts 
            maxPts.append(Partition(R[i]))

        mp = np.array(maxPts)

        xMax = np.argmax(mp[:,1])
        yMax = np.argmax(mp[:,3])

        # determine line type
        if (mp[yMax][3] > mp[xMax][1]):
            lineType = 'h'
            coord = mp[yMax][2]
        elif (mp[yMax][3] < mp[xMax][1]):
            lineType = 'v'
            coord = mp[xMax][0]
        else:
            lineType = 'v'
            coord = mp[xMax][2]

        L = [lineType, coord]
        S.append(L)
        BoundedRects(L)
        Plot()

def Initialize(fileNm):
    global numPoints
    # load the instance file
    points = np.loadtxt(fileNm, skiprows=1, dtype=int)

    xMax = max(points[:,0])
    yMax = max(points[:,1])
    BaseRect = Rectangle(0, 0, xMax, yMax)
    R.append(BaseRect)

    numPoints = len(points)

    # add the points from the file into the Rectangle points list
    for i in range(0, len(points)):
        p = Point(i, points[i][0], points[i][1])
        R[0].points.append(p)



Initialize('instance01.csv')
CreateLines()


print("Done")