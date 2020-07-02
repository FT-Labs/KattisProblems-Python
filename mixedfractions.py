"""
Author : Arda
Date : 7/2/2020
"""

from fractions import Fraction

x,y = [int(x) for x in input().split()]

while x and y:
    t = int(x/y)

    print(f"{t} {x-t*y} / {y}")


    x, y = [int(x) for x in input().split()]