#!/usr/bin/env python3
"""
Author : Arda
Company : PhysTech
Date : 2020-09-09
"""


spies = list()
houses = list()


for i in range(int(input())):

    l = [x for x in input()]

    for x in range(len(l)):
        if l[x] == "S":
            spies.append([i,x])
    for x in range(len(l)):
        if l[x] == "H":
            houses.append([i, x])


minPaths = dict()


for i in range(len(spies)):
    for house in houses:

        path = abs(spies[i][0]-house[0])+abs(spies[i][1]-house[1])

        if i in minPaths:
            if path<minPaths[i]:
                minPaths[i] = path
        else:
            minPaths[i] = path

print(max(minPaths.values()))









