"""
Author : Arda
Date : 7/18/2020
"""

e,f,c = [int(x) for x in input().split()]

totalDrinked = int((e+f)/c)

remaining = (e+f)%c

tmp = totalDrinked+remaining

while tmp>0:
    if tmp>c:
        q = tmp%c
    else:
        q = 0
    totalDrinked += tmp//c
    tmp //= c
    tmp += q



print(totalDrinked)


