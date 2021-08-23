import math

#Using strings because of cpu time limit
f = {'1': 1, '2': 2, '6': 3, '24': 4, '120': 5, '720': 6, '5040': 7, '40320': 8, '362880': 9, '3628800': 10}
n = str(input())

if n in f:
    print(str(f[n]))
else:
    l = len(n)
    x = 0
    for i in range(1,l*2):
        x += math.log10(i)
        if x>l:
            print(str(i-1))
            break