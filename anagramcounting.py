#!/usr/bin/python

from math import factorial as f
import sys
from collections import Counter


for line in sys.stdin:
    line = line.rstrip(" \n")
    cnt  = len(line)
    l = list(line)
    ans = f(cnt)

    for c in Counter(l).most_common():
        if(c[1] < 2):
            break
        else:
            ans //= f(c[1])

    print(int(ans))
