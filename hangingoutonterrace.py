#!/usr/bin/env/python3
"""
Author : Arda
Company : PhysTech
Date : '24.06.2020'
"""

size , loopTime = [int(_) for _ in input().split()]

cnt = 0
total = 0
for i in range(loopTime):

    cond , n = input().split()

    if cond == "enter":
        if total+int(n)>size:
            cnt += 1
        else:
            total += int(n)
    elif cond == "leave":
        total -= int(n)

print(cnt)

