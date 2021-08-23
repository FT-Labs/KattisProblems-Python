"""
Author : Arda
Date : 7/10/2020
"""
from math import pi

r,m,c = [float(x) for x in input().split()]

while r or m or c:
    print(f"{pi*r**2} {4*r**2*c/m}")
    r, m, c = [float(x) for x in input().split()]