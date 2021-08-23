"""
Author : Arda
Date : 6/25/2020
"""

l = int(input())
d = int(input())
x = int(input())
n = l

while n<=d:
    digitsum = sum([int(x) for x in str(n)])

    if digitsum==x:
        print(n)
        break
    n+=1

n = d

while n>=l:
    digitsum = sum([int(x) for x in str(n)])

    if digitsum==x:
        print(n)
        break

    n-=1