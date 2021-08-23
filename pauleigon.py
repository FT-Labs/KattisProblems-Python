"""
Author : Arda
Date : 7/11/2020
"""

n,p,q = [int(x) for x in input().split()]


cnt = int((p+q)/n)


print("paul" if cnt%2==0 else "opponent")
