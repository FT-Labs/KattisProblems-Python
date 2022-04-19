#!/usr/bin/env python

ops = ['*', '+', '-', '/']

x1, x2, x3, x4 = input().split()

ans = list()

for i in ops:
    for j in ops:
        try:
            if (int(eval(x1+i+x2)) == int(eval(x3+j+x4))):
                ans.append(f"{x1} {i} {x2} = {x3} {j} {x4}")
        except ZeroDivisionError:
            pass

if len(ans) > 0:
    print("\n".join(ans))
else:
    print("problems ahead")
