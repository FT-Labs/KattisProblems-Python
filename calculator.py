#!/usr/bin/python


import sys

for line in sys.stdin:
    line = line.strip("\n")
    print(f"{float(eval(line)):.2f}")
