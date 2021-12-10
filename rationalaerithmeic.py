#!/usr/bin/python

from fractions import Fraction


x = int(input())

for i in range(x):
    x1, y1, op, x2, y2 = input().split()
    f1 = Fraction(int(x1), int(y1))
    f2 = Fraction(int(x2), int(y2))

    if op == '+':
        ans = f1 + f2
    elif op == '-':
        ans = f1 - f2
    elif op == '/':
        ans = f1 / f2
    else:
        ans = f1 * f2

    print(f"{ans.numerator} / {ans.denominator}")
