#!/usr/bin/env python3
"""
Author : Arda
Company : PhysTech
Date : 10.09.2020
"""



n,t = [float(x) for x in input().split()]

while n and t:
    q = 2**n

    for i in range(int(n)-1,-1,-1):
        prize = 2**i
        ans = prize / q
        if ans <= t:
            q = (t + 1) / 2 * q
        else:
            q = (ans - t) / (1 - t) * prize + (1 - ans) / (1 - t) * (ans + 1) / 2 * q

    print("{:.3f}".format(q))

    n, t = [float(x) for x in input().split()]