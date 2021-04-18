

def MAX_PAIRS(A):

    min = -1
    cur = -1
    maxVals = []
    minValsIdx = []
    minIdx = -1

    # find the pairs
    for i in range(0,len(A)):
        if (min == -1):
            min = A[i]
            minIdx = i
        elif (A[i] < min):
            min = A[i]
            minIdx = i

        minValsIdx.append(minIdx)
        maxVals.append(A[i]-min)

    # determine the maximum pair
    max = -1
    maxIdx = -1
    for j in range(0, len(A)):
        if (maxVals[j] > max):
            max = maxVals[j]
            maxIdx = j

    return minValsIdx[maxIdx], maxIdx


#A = [5,9,1,4,7,2]
#A = [5,9,7,4,1,2,10,8,5,12]
A = [10,3,5,4,1,11,14,4,3,8]
#A = [5,20,6,7,5,3,1,6,4]
print(MAX_PAIRS(A))
