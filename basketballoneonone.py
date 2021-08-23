"""
Author : Arda
Date : 7/10/2020
"""

a = 0
b = 0

s = input()
for i in range(0,len(s),2):
    if s[i]=="A":
        a += int(s[i+1])
    else:
        b += int(s[i+1])

print("A" if a>b else "B")