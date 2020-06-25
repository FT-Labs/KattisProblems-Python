"""
Author : Arda
Date : 6/25/2020
"""
from math import radians,sin,cos

rep = int(input())
g = 9.81

for _ in range(rep):
    v,theta,x,h1,h2 = [float(x) for x in input().split()]

    t = x/(v*cos(radians(theta)))

    y = v*t*sin(radians(theta))-0.5*g*t**2

    if y-1<=h1 or y+1>=h2:
        print("Not safe")
    else:
        print("Safe")