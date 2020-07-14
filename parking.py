"""
Author : Arda
Date : 7/13/2020
"""

q = [int(x) for x in input().split()]


times = []
for _ in range(3) :
    times.append([int(x) for x in input().split()])
times.sort()

tot = 0

for i in range(1,101):
    n = 0
    for j in range(3):
        if times[j][0] <= i < times[j][1]:
            n += 1
    tot += q[n-1]*n

print(tot)