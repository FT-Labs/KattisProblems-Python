"""
Author : Arda
Date : 7/27/2020
"""
def find_adjacentes(xVal , yVal):
    nextPoint = 0
    points = [[xVal+2,yVal+1],[xVal+2,yVal-1],[xVal-2,yVal+1],[xVal-2,yVal-1],[xVal+1,yVal+2],[xVal+1,yVal-2],[xVal-1,yVal+2],[xVal-1,yVal-2]]

    for point in points:
        if point[0]<0 or point[1]<0 or point[0]>=len(mat[0])-1 or point[1]>= len(mat[0])-1 or mat[point[0]][point[1]] == "#" or passedPoints[point[0]][point[1]]:
            continue

        passedPoints[point[0]][point[1]] = True
        x.append(point[0])
        y.append(point[1])
        nextPoint += 1

    return nextPoint


mat = []
stepCounter = 0
leftPoints = 1
nextPoints = 0
isComplete = False

cnt = 0
for _ in range(int(input())):
    arr = [ch for ch in input()]
    if "K" in arr:
        start = (cnt,arr.index("K"))
    mat.append(arr)
    cnt += 1

passedPoints = [[False for x in range(len(mat[0]))] for y in range(len(mat[0]))]

x = [start[0]]
y = [start[1]]
mat[0][0] = "E"

while x or y:
    xV = x.pop(0)
    yV = y.pop(0)

    nextPoints += find_adjacentes(xV,yV)
    leftPoints -= 1

    if mat[xV][yV] == "E":
        print(stepCounter)
        isComplete = True
        break


    if leftPoints == 0:
        leftPoints = nextPoints
        nextPoints = 0
        stepCounter += 1

if not isComplete:
    print(-1)
