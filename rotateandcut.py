"""
Author : Arda
Date : 7/10/2020
"""

#UNDONE
from math import ceil

for _ in range(int(input())):
    r,s = input().split()

    for q in range(int(r)):
        cut = 0 if len(s) < 4 else ceil(len(s) / 4)
        if cut==0:
            break

        if q%2==0:
            s = s[cut:]
        else:
            s = s[:-cut]

    print(s)
