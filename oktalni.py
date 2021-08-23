"""
Author : Arda
Date : 7/13/2020
"""

x = input()[::-1]

tot = 0


for i in range(len(x)):

    tot += 2**i if x[i]!='0' else 0

s = ""

while tot>0:
    tmp = tot%8
    s += str(tmp)

    tot //= 8


print(s[::-1])