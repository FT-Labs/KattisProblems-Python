#!/usr/bin/python

import sys

l = []

for line in sys.stdin:
    line = line.strip("\n")
    l += line.split(" ")


from itertools import combinations, permutations

s = set()

for comb in combinations(l, 2):
    st = "".join(comb)
    s.add(st)
    st = "".join(comb[::-1])
    s.add(st)

l = list(s)
l.sort()

print("\n".join(l))
