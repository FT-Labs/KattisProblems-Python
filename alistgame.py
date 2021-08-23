"""
Author : Arda
Date : 6/25/2020
"""

x = int(input())

times = 1
counter = 0

while times**2<=x:
    if x%times==0:
        x /= times
        counter += 1
    else:
        times += 1
    if times == 1 : times += 1

print(counter)