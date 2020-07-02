"""
Author : Arda
Date : 7/2/2020
"""

people = int(input())

order = ["1" for x in range(people)]

p = [int(x) for x in input().split()]

for i in range(2,people+1):
    order[p[i-2]+1] = str(i)

print(" ".join(order))