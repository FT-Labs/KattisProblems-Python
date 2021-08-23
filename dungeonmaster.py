def find_adjacentes(xVal , yVal , zVal):
    nextPoint = 0
    points = [[xVal - 1, yVal , zVal], [xVal + 1, yVal , zVal], [xVal, yVal - 1 , zVal], [xVal, yVal + 1 , zVal] , [xVal , yVal , zVal +1] , [xVal,yVal,zVal-1]]

    for point in points:
        if point[0]<0 or point[1]<0 or point[2]<0 or point[0]>=dungeonParameters[1] or point[1]>= dungeonParameters[2] or point[2]>= dungeonParameters[0] \
            or levels[point[2]][point[0]][point[1]] == "#" or passedPoints[point[2]][point[0]][point[1]] == True:
            continue

        passedPoints[point[2]][point[0]][point[1]] = True
        xValues.append(point[0])
        yValues.append(point[1])
        zValues.append(point[2])
        nextPoint += 1

    return nextPoint



while True:
    dungeonParameters = [int(x) for x in input().split(" ")]

    if all(dungeonParameters) == 0:
        break
    levels = [[["." for col in range(1)] for row in range(dungeonParameters[1])] for x in range(dungeonParameters[0])]
    passedPoints = [[[False for _ in range(dungeonParameters[2])] for z in range(dungeonParameters[1])] for x in range(dungeonParameters[0])]

    for i in range(dungeonParameters[0]):
        lev = []
        for j in range(dungeonParameters[1]):
            lev.append([x for x in input()])
        levels[i] = lev
        input()

    start = [0,0,0]
    for z in range(dungeonParameters[0]):
        for x in range(dungeonParameters[1]):
            for y in range(dungeonParameters[2]):
                if levels[z][x][y] == "S":
                    start = [x,y,z]

    xValues = [start[0]]
    yValues = [start[1]]
    zValues = [start[2]]
    stepCounter = 0
    leftPoints = 1
    nextPoints = 0
    isComplete = False


    while len(xValues)>0 or len(yValues)>0 or len(zValues)>0:

        x = xValues.pop(0)
        y = yValues.pop(0)
        z = zValues.pop(0)

        nextPoints += find_adjacentes(x,y,z)
        leftPoints -= 1

        if levels[z][x][y] == "E":
            print("Escaped in {} minute(s).".format(stepCounter))
            isComplete = True
            break

        if leftPoints == 0:
            leftPoints = nextPoints
            nextPoints = 0
            stepCounter += 1

    if not isComplete:
        print("Trapped!")