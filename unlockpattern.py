"""
Author : Arda
Date : 7/18/2020
"""

from math import hypot

x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]
z = [int(x) for x in input().split()]

rows = [x,y,z]

total = 0
memo = 0
q = True
while True:
    if memo==10:
        break
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] == 1 and q:
                memo = 2
                loc = (i,j)
                q = False
            elif rows[i][j] == memo:

                memo += 1
                total += hypot(abs(i-loc[0]),abs(j-loc[1]))
                loc = (i,j)


print(total)