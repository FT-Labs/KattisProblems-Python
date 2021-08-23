"""
Author : Arda
Date : 6/25/2020
"""

rep = int(input())

for _ in range(rep):
    ispossible = False
    x,y,z = [(int(q)) for q in input().split()]

    if x+y==z:
        print("Possible")
    elif x-y==z or y-x==z:
        print("Possible")
    elif x*y==z:
        print("Possible")
    elif x/y==z or y/x==z:
        print("Possible")
    else:
        print("Impossible")
