import os
import re
import numpy as np
import random
import matplotlib.pyplot as plt
import statistics

S = []
R = []

# TODO: remove this and its references 
numPoints = 0

# A data structure for a rectangle
class Rectangle:
	
	# Constructor to create a new rectangle
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

    # compare the points in the existing rectangle and see if they need to be moved
    # to the new one
    for i in range(0, len(OriginalRect.points)):
        pt = OriginalRect.points[i]
        
        if ((LineType == 'h' and (pt.y < OriginalRect.y1 or pt.y > OriginalRect.y2)) or
           (LineType == 'v' and (pt.x < OriginalRect.x1 or pt.x > OriginalRect.x2))):
            ToBeMoved.append(pt)
    
    # move the points that need to go with the new rectangle
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

# algorithm to decide where to draw lines to maximize point separation
def Partition(Rect):
    pts = len(Rect.points)
    
    if (pts == 0):
        return (0,0,0,0,0)

   # use the median of the point's x and y coords in the rectangle as our separator 
   # to split local clusters 
    x = []
    y = []
    for i in range(0, pts):
        x.append(Rect.points[i].x)
        y.append(Rect.points[i].y)

    medX = statistics.median(x)
    meanX = statistics.mean(x)
    if (not medX % 1):     
        if (meanX <  medX and medX > 1): 
            medX -= 0.5
        else:
            medX += 0.5

    medY = statistics.median(y)
    meanY = statistics.mean(y)
    if (not medY % 1):
        if (meanY <  medY and medY > 1): 
            medY -= 0.5
        else:
            medY += 0.5

    xRight = 0
    xLeft = 0
    yAbove = 0
    yBelow = 0
    for j in range(0, pts):
        if (Rect.points[j].x > medX): xRight += 1
        if (Rect.points[j].x < medX):  xLeft += 1
        if (Rect.points[j].y > medY):  yAbove += 1
        if (Rect.points[j].y < medY):  yBelow += 1

    #return (medX, max(xRight, xLeft), medY, max(yAbove, yBelow))
    return (medX, max(xRight, xLeft), medY, max(yAbove, yBelow), len(Rect.points))
    
# test to see if there are more points to be separated
def Done():
    
    done = True
    for i in range(0, len(R)):
        if (len(R[i].points) > 1):
            done = False
            break

    return done

# main algorithm to divide the base rectangle into smaller ones by 
# creating axis-parallel lines
def CreateLines():
    while (Done() != True):
    
        maxPts = []

        # partition returned as tuples of (x-coord, # x pts, y-coord, # y pts, total points)
        for i in range(0,len(R)):
            part = list(Partition(R[i]))
            # check for duplication against our list of lines
            for j in range(0, len(S)):
                if (S[j][0] == 'v' and S[j][1] == part[0]):
                    part[1] = 0
                if (S[j][0] == 'h' and S[j][1] == part[2]):
                    part[3] = 0
            maxPts.append(part)

        mp = np.array(maxPts)

        # get the index of the x,y max points in mp
        Max  = np.argmax(mp[:,4])
        #xMax = np.argmax(mp[:,1])
        #yMax = np.argmax(mp[:,3])

        # determine line type and its axis coordinate
        if (mp[Max][3] < mp[Max][1]):
            lineType = 'v'
            coord = mp[Max][0]
        elif (mp[Max][3] > mp[Max][1]):
            lineType = 'h'
            coord = mp[Max][2]
        else:
            if (len(S) == 0):
                lineType = 'v'
                coord = mp[Max][0]
            elif (len(S) == 1):
                lineType = 'h'
                coord = mp[Max][2]
            else:
                ran = random.randint(0,1)
                if (ran == 1):
                    lineType = 'v'
                    coord = mp[Max][0]
                else:
                    lineType = 'h'
                    coord = mp[Max][2]

        # add the new line to our list of lines
        L = (lineType, coord)
        S.append(L)
        # split rectangles as necessary based on our new line
        # and adjsut points to the correct rectangle
        BoundedRects(L)
    
        # TODO: remove for submission
        #Plot()

def Initialize(fileNm):
    global numPoints, S, R

    S = []  # set of vertical or horizontal lines
    R = []  # collection of rectangles

    # load the instance file
    points = np.loadtxt(fileNm, skiprows=1, dtype=int)

    # use the maximum coordinates to create an initial base rectangle that will be 
    # divided into smaller rectangles in CreateLines
    xMax = max(points[:,0])
    yMax = max(points[:,1])
    BaseRect = Rectangle(0, 0, xMax, yMax)
    R.append(BaseRect)

    # TODO: remove for submission
    numPoints = len(points)

    # add the points from the file into the base Rectangle 
    for i in range(0, len(points)):
        p = Point(i, points[i][0], points[i][1])
        R[0].points.append(p)

# Write the results to a file
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
    
    # Handle multiple inputs by looping through files in the directory
    for filename in os.listdir(path):
        if re.match("instance\d+", filename):
            with open(os.path.join(path, filename), 'r') as f:
                Initialize(f)
                CreateLines()
                WriteResults(filename)

if __name__ == "__main__":
    main()