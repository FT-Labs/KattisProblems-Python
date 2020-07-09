"""
Author : Arda
Date : 7/10/2020
"""

from string import ascii_lowercase

dc = dict()

for i in range(len(ascii_lowercase)):
    dc[ascii_lowercase[i]] = i

r,c = [int(x) for x in input().split()]

m = [["" for x in range(r)] for j in range(c)]

ans = dict()

for _ in range(r):
    x = input()

    for i in range(len(x)):
        m[_][i] = x[i]

for row in m:
    s = ""
    for q in row:
        if q!= "#":
            s += q
        elif row[-1] == q and q!= "#":
            tot = 0

            for i in row:
                tot += dc[i]
            ans[s] = tot
        else:
            if len(s)>=2:
                tot = 0
                for i in row:
                    tot += dc[i]
                ans[s] = tot
            s = ""

print(ans)
for i in range(r):
    print([row[i] for row in m])

