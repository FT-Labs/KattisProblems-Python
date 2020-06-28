"""
Author : Arda
Date : 6/27/2020
"""

x,y,z = [int(x) for x in input().split()]

if x+y==z:
    print(f"{x}+{y}={z}")
elif y+z==x:
    print(f"{x}={y}+{z}")
elif x-y==z:
    print(f"{x}-{y}={z}")
elif y-z==x:
    print(f"{x}={y}-{z}")
elif x*y==z:
    print(f"{x}*{y}={z}")
elif y*z==x:
    print(f"{x}={y}*{z}")
elif x/y==z:
    print(f"{x}/{y}={z}")
elif y/z==x:
    print(f"{x}={y}/{z}")

