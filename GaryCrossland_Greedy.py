import os
import re
import numpy as np
import random

S = []
R = []

# TODO: remove this and its references 
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
    pts = len(Rect.points)
    
    if (pts == 0):
        return (0,0,0,0)

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
        meanX = int(ux/pts)
        meanY = int(uy/pts) 

    xAbove = 0
    xBelow = 0
    yAbove = 0
    yBelow = 0
    for j in range(0, pts):
        if (Rect.points[j].x > meanX):  xAbove += 1
        if (Rect.points[j].x < meanX):  xBelow += 1
        if (Rect.points[j].y > meanY):  yAbove += 1
        if (Rect.points[j].y < meanY):  yBelow += 1

    xRandom = random.randint(0,1) - 0.5
    yRandom = random.randint(0,1) - 0.5

    return (meanX + xRandom, max(xAbove, xBelow), meanY + yRandom, max(yAbove, yBelow))

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
            ran = random.randint(0,1)
            if (ran == 1):
                lineType = 'v'
                coord = mp[xMax][0]
            else:
                lineType = 'h'
                coord = mp[yMax][2]

        L = (lineType, coord)

        S.append(L)
        BoundedRects(L)

def Initialize(fileNm):
    global numPoints, S, R

    S = []
    R = []

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

def WriteResults(filename):
    number = re.findall('[0-9]+', filename)
    fname = "greedy_solution" + number[0]
    with open(fname, 'w') as f:
        f.write('{x}\n'.format(x=len(S)))
        output = np.array(S)
        for l in range(0,len(output)):
            f.write('{x} {y}\n'.format(x=output[l][0],y=output[l][1]))
        f.close()

def main():
    path = "./"
    for filename in os.listdir(path):
        if re.match("instance\d+", filename):
            with open(os.path.join(path, filename), 'r') as f:
                Initialize(f)
                CreateLines()
                WriteResults(filename)

if __name__ == "__main__":
    main()