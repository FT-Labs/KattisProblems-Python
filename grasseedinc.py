"""
Author : Arda
Date : 6/25/2020
"""

cost = float(input())
rep = int(input())

total = 0.

for _ in range(rep):
    w,h = [float(x) for x in input().split()]
    total += w*h*cost

print("{:.7f}".format(total))