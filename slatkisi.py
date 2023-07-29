#!/usr/bin/python

from math import ceil


x, y = map(int, input().split())

div = 10**y

cur = round(x/div)

print(cur * div)
