"""
Author : Arda
Date : 7/10/2020
"""

from string import ascii_lowercase

dc = dict()

for i in range(len(ascii_lowercase)):
    dc[ascii_lowercase[i]] = i

r,c = [int(x) for x in input().split()]

m = [["" for x in range(c)] for j in range(r)]

ans = dict()

for _ in range(r):
    x = input()

    for i in range(c):
        m[_][i] = x[i]

arr = []

for row in m:
     s = ""
     for ch in row:
         if ch!="#":
             s += ch
         else:
             if len(s)>=2:
                 arr.append(s)
             s = ""
     if len(s)>=2: arr.append(s)

try:
    for i in range(r):
        s = ""
        for ch in [row[i] for row in m]:
            if ch != "#":
                s += ch
            else:
                if len(s) >= 2:
                    arr.append(s)
                s = ""
        if len(s) >=2 : arr.append(s)
except:
    pass


print(sorted(arr)[0])

