#!/usr/bin/env python

from math import log, pow

n = int(input())

def f(x, C):
    return x**x - C

def dx(x):
    return (log(x)+1)*x**x

x0 = 1

while f(x0, n) < 0:
    x0 += 1

while True:
    xtmp = x0 - f(x0, n) / dx(x0)

    if abs(xtmp - x0) <= 1e-6:
        break

    x0 = xtmp


print(xtmp)
