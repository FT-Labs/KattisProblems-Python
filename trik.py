"""
Author : Arda
Date : 6/25/2020
"""

a,b,c = "B",".","."

s = input()

for ch in s:
    if ch=="A":
        a,b = b,a
    elif ch=="B":
        b,c = c,b
    elif ch=="C":
        a,c = c,a

if a=="B":
    print(1)
elif b=="B":
    print(2)
elif c=="B":
    print(3)


