#!/usr/bin/python

from math import hypot

x1, y1, x2, y2, x1e, y1e, x2e, y2e = map(int, input().split())


mx = max(hypot(x2-x1, y2-y1), hypot(x2e-x1e, y2e-y1e))


print(mx)
