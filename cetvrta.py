"""
Author : Arda
Date : 6/25/2020
"""
from collections import Counter

x = []
y = []

for _ in range(3):
    i,j = [int(z) for z in input().split()]
    x.append(i)
    y.append(j)

print(Counter(x).most_common()[1][0],Counter(y).most_common()[1][0])