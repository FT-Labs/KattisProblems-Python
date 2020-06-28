"""
Author : Arda
Date : 6/27/2020
"""

s = 0

n = int(input())

while n!=0:
    l = [input() for _ in range(n)]
    nl = []

    for i in range(0,n,2):
        nl.append(l[i])
    if n%2!=0:
        for i in range(n-2,0,-2):
            nl.append(l[i])
    else:
        for i in range(n-1,0,-2):
            nl.append(l[i])

    s += 1
    print("SET {}".format(s))
    for i in nl : print(i)

    n = int(input())
