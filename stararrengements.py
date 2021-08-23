"""
Author : Arda
Date : 7/10/2020
"""

n = int(input())


print(f"{n}:")

x = 2
y = 1

arr = []
while x+y<=n:

    tot = 0
    tot1 = 0

    while tot<=n:

        tot += x
        tot1 += x
        if tot == n:
            arr.append((x,y))

        if tot1 == n:
            arr.append((x, y+1))

        tot1 += y+1
        tot += y
        if tot == n:
            arr.append((x, y))
        if tot1 == n:
            arr.append((x, y+1))

    x += 1
    y += 1

for i in sorted(arr,key=lambda z : z[1]):
    print(f"{i[0]},{i[1]}")






