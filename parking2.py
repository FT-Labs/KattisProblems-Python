"""
Author : Arda
Date : 6/27/2020
"""

rep = int(input())

for _ in range(rep):
    dist = 0
    sLen = int(input())
    slots = sorted([int(x) for x in input().split()])
    mean = int(sum(slots)/sLen)
    start = mean

    for i in slots:
        dist += abs(start-i)
        start = i

    print(dist+slots[-1]-mean)


