#!/usr/bin/python


from collections import Counter

input()


l = map(int, input().split())


c = Counter(l)

s = ""
for i in c.most_common():
    s += f"{i[0]} "*i[1]

print(s)
