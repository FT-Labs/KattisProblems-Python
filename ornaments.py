#!/usr/bin/env python

import math as m

r, h, s = map(int, input().split())

while (r+h+s) != 0:
    tot = 2 * m.sqrt(h**2 - r**2)

    ang = 360 - 2 * m.acos(r/h) * (180 /m.pi)
    tot += 2 * m.pi * (ang / 360) * r
    tot += tot * (s / 100)

    print("{:.2f}".format(tot))
    r, h, s = map(int, input().split())
