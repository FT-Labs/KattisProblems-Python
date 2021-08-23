"""
Author : Arda
Date : 6/28/2020
"""

for _ in range(int(input())):
    k,b,n = [int(x) for x in input().split()]
    ssd = 0
    while n>0:
        ssd += (n%b)**2
        n /= b
        n = int(n)
    print(f"{k} {ssd}")