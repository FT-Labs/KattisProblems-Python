#!/usr/bin/python

n, k = map(int, input().split())


pokes = []

for i in range(n):
    a, d, h = map(int, input().split())
    pokes.append((a, d, h))


highAttack = sorted(pokes, key=lambda x : x[0], reverse=True)
highDefense = sorted(pokes, key=lambda x : x[1], reverse=True)
highHealth = sorted(pokes, key=lambda x : x[2], reverse=True)




cnt = 0

s = set()
for i in range(k):
    s.update([highHealth[i], highAttack[i], highDefense[i]])
    cnt = len(s)


print(cnt)
