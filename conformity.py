#!/usr/bin/python

from collections import Counter


n = int(input())

l = {}
mx = 0

for _ in range(n):
    li = list(map(str, input().split()))
    li.sort()

    if "".join(li) in l:
        l["".join(li)] += 1
    else:
        l["".join(li)] = 1
    mx = max(mx, l["".join(li)])



ans = 0
for key, val in l.items():
    if val == mx:
        ans += mx

print(ans)
