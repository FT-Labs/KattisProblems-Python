"""
Author : Arda
Date : 7/2/2020
"""

for _ in range(int(input())):

    k,n = [int(x) for x in input().split()]

    print("{} {} {} {}".format(k,int(n*(n+1)/2),(n-1)*(n+1)+1,n*(n+1)))