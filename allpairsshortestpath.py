"""
Author : Arda
Date : 7/19/2020
"""

from math import inf

#IMPORTANT!!! You won't get past through execution time with Python in this question. This is the most efficient way i could find.
#If you want to get past through execution time, please write this code in C++.

def floyd(m,N):
    # Floyd algorithm for finding shortest distance between all pairs

    loopTime = N
    m0 = m

    for k in range(loopTime):
        for i in range(loopTime):
            for j in range(loopTime):
                if m0[i][j] > m0[i][k] + m0[k][j]:
                    m0[i][j] = m0[i][k] + m0[k][j]

    # Searching for any edge < 0, if exists, there is a negative cycle
    # Since answer is not important, no need to use bellman-ford for more efficiency

    for i in range(loopTime):
        for j in range(loopTime):
            for k in range(loopTime):
                if m0[k][k]<0 and m0[i][k]!= inf and m0[k][j]!= inf:
                    m0[i][j] = inf

    return m0


m = [[inf for x in range(151)] for y in range(151)]

N,M,Q = [int(x) for x in input().split()]


while N or M or Q:

    for _ in range(M):
        s,d,w = [int(x) for x in input().split()]
        m[s][d] = w

    mRelaxed = floyd(m,N)
    for i in range(N):
        mRelaxed[i][i] = 0

    for _ in range(Q):
        start,dest = [int(x) for x in input().split()]


        if mRelaxed[start][dest]>=inf:
            print("Impossible")
        elif mRelaxed[start][dest]<=-inf:
            print("-Infinity")
        else:
            print(mRelaxed[start][dest])

    print()

    N,M,Q = [int(x) for x in input().split()]


