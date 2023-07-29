#!/usr/bin/python

from itertools import combinations

n = int(input())

sour = []
bitter = []

for i in range(n):
    s, b = [int(x) for x in input().split()]
    sour.append(s)
    bitter.append(b)


mn = 100000000

for i in range(n):

    for s,b in zip(combinations(sour, i+1), combinations(bitter,i+1)):
        mul = 1
        for j in s:
            mul *= j
        sm = sum(b)


        mn = min(mn, abs(mul - sm))

        if mn == 0:
            break


print(mn)
