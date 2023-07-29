#!/usr/bin/env python3
"""
Author : Arda
Company : PhysTech
Date : 15.09.2020
"""

import sys

size , rang = [int(x) for x in input().split()]

allRooms = [i for i in range(1,size+1)]
rooms = []
for i in range(rang):
    rooms.append(int(input()))


for i in allRooms:
    if i not in rooms:
        print(i)
        sys.exit()

print("too late")


